#!/usr/bin/env python3
# ──────────────────────────────────────────────────────────────
# [INPUT]: 依赖 api.github.com REST 接口，重写 README.md 的
#          <!-- activity starts/ends --> 标记区
# [OUTPUT]: 原地更新 README.md（仅标记区，手写内容不触碰）
# [POS]:    Profile 自动化脚本，由 .github/workflows/build.yml 每日执行
# [PROTOCOL]: When making changes, update this header first, then check CLAUDE.md
# ──────────────────────────────────────────────────────────────
import json
import os
import pathlib
import re
import urllib.request
from datetime import datetime, timedelta, timezone

API = "https://api.github.com"
ENDPOINTS = (
    f"{API}/orgs/ziweiknows/repos",
    f"{API}/users/ruijayfeng/repos",
)
SELF_REPO = "ruijayfeng/ruijayfeng"
SKIP_REPOS = {"ziweiknows/.github", "ziweiknows/demo-repository"}
TOP_N = 6
ACTIVITY_DAYS = 14
MIN_COMMITS = 2
DESC_LIMIT = 70


def get(url):
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "readme-bot",
    }
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.headers, json.load(resp)


def fetch_json(url):
    return get(url)[1]


def recent_commit_count(full_name):
    """Count commits in the last ACTIVITY_DAYS via the Link header's 500-page hint."""
    since = datetime.now(timezone.utc) - timedelta(days=ACTIVITY_DAYS)
    url = f"{API}/repos/{full_name}/commits?per_page=1&anon=true&since={since.isoformat()}"
    headers, _ = get(url)
    link = headers.get("Link", "")
    if 'rel="last"' in link:
        return int(link.split("page=")[-1].split(">")[0])
    body = fetch_json(url)
    return len(body)


def collect_activity():
    repos = []
    for base in ENDPOINTS:
        page = 1
        while True:
            batch = fetch_json(f"{base}?per_page=100&page={page}")
            repos.extend(batch)
            if len(batch) < 100:
                break
            page += 1
    alive = [
        r for r in repos
        if not r["fork"]
        and r["full_name"] not in SELF_REPO
        and r["full_name"] not in SKIP_REPOS
        and r["pushed_at"][:10] >= (datetime.now(timezone.utc) - timedelta(days=ACTIVITY_DAYS)).strftime("%Y-%m-%d")
    ]
    alive.sort(key=lambda r: r["pushed_at"], reverse=True)
    lines = []
    for r in alive:
        if len(lines) >= TOP_N:
            break
        try:
            commits = recent_commit_count(r["full_name"])
        except Exception as err:
            print(f"skip {r['full_name']}: {err}")
            continue
        if commits < MIN_COMMITS:
            continue
        desc = (r.get("description") or "").strip()
        if len(desc) > DESC_LIMIT:
            desc = desc[:DESC_LIMIT].rsplit(" ", 1)[0] + "…"
        row = f"- [{r['name']}]({r['html_url']}) - ★{r['stargazers_count']} · {commits} commits/{ACTIVITY_DAYS}d"
        if desc:
            row += f" · {desc}"
        lines.append(row)
    return lines


def main():
    lines = collect_activity()
    if not lines:
        raise SystemExit("no active repos found - refusing to blank the section")
    readme = pathlib.Path(__file__).parent.resolve() / "README.md"
    text = readme.read_text(encoding="utf-8")
    pattern = re.compile(
        r"(<!-- activity starts -->\n).*?(\n<!-- activity ends -->)",
        re.S,
    )
    if not pattern.search(text):
        raise SystemExit("markers '<!-- activity starts/ends -->' not found in README.md")
    new_text = pattern.sub(lambda m: m.group(1) + "\n".join(lines) + m.group(2), text, count=1)
    readme.write_text(new_text, encoding="utf-8")
    print(f"updated activity section with {len(lines)} entries")


if __name__ == "__main__":
    main()
