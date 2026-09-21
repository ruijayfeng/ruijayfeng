#!/usr/bin/env python3
# ──────────────────────────────────────────────────────────────
# [INPUT]: 依赖 api.github.com REST 接口，重写 README.md 的
#          <!-- releases starts/ends --> 标记区
# [OUTPUT]: 原地更新 README.md（仅标记区，手写内容不触碰）
# [POS]:    Profile 自动化脚本，由 .github/workflows/build.yml 每日执行
# [PROTOCOL]: When making changes, update this header first, then check CLAUDE.md
# ──────────────────────────────────────────────────────────────
import json
import os
import pathlib
import re
import urllib.request

API = "https://api.github.com"
ENDPOINTS = (
    f"{API}/orgs/ziweiknows/repos",
    f"{API}/users/ruijayfeng/repos",
)
SELF_REPO = "ruijayfeng/ruijayfeng"
TOP_N = 8


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
        return json.load(resp)


def list_repos():
    for base in ENDPOINTS:
        page = 1
        while True:
            batch = get(f"{base}?per_page=100&page={page}")
            for r in batch:
                if not r["fork"] and r["full_name"] != SELF_REPO:
                    yield r["full_name"]
            if len(batch) < 100:
                break
            page += 1


def collect_releases():
    items = []
    for full in list_repos():
        try:
            releases = get(f"{API}/repos/{full}/releases?per_page=5")
        except Exception as err:
            print(f"skip {full}: {err}")
            continue
        repo = full.split("/")[-1]
        for rel in releases:
            if rel.get("draft"):
                continue
            date = (rel.get("published_at") or "")[:10]
            if not date:
                continue
            items.append((date, f"- [{repo} {rel['tag_name']}]({rel['html_url']}) - {date}"))
    items.sort(key=lambda x: x[0], reverse=True)
    return [line for _, line in items[:TOP_N]]


def main():
    lines = collect_releases()
    if not lines:
        raise SystemExit("no releases found - refusing to blank the section")
    readme = pathlib.Path(__file__).parent.resolve() / "README.md"
    text = readme.read_text(encoding="utf-8")
    pattern = re.compile(
        r"(<!-- releases starts -->\n).*?(\n<!-- releases ends -->)",
        re.S,
    )
    if not pattern.search(text):
        raise SystemExit("markers '<!-- releases starts/ends -->' not found in README.md")
    new_text = pattern.sub(lambda m: m.group(1) + "\n".join(lines) + m.group(2), text, count=1)
    readme.write_text(new_text, encoding="utf-8")
    print(f"updated releases section with {len(lines)} entries")


if __name__ == "__main__":
    main()
