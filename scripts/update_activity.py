#!/usr/bin/env python3
"""Render a locally hosted profile chart from public GitHub commits."""
import json
import os
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

USER = "deniziuss"
DEST = Path(__file__).resolve().parents[1] / "assets/profile/activity.svg"
LIGHT = {"bg":"#F5F5F7","ink":"#1D1D1F","muted":"#626269","line":"#D9D9DF","empty":"#E5E5EA","a1":"#B9D9FC","a2":"#75B9FC","a3":"#0071E3","a4":"#0052A3","accent":"#0066CC"}
DARK = {"bg":"#161618","ink":"#F5F5F7","muted":"#A1A1A6","line":"#39393D","empty":"#29292D","a1":"#183C63","a2":"#215F9D","a3":"#2997FF","a4":"#80C2FF","accent":"#64B0FF"}

def api(path):
    headers = {"Accept":"application/vnd.github+json",
               "User-Agent":"deniziuss-profile-chart",
               "X-GitHub-Api-Version":"2022-11-28"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    try:
        with urlopen(Request("https://api.github.com"+path, headers=headers), timeout=30) as response:
            return json.load(response)
    except HTTPError as exc:
        if exc.code == 409 and "/commits?" in path:
            return []
        raise RuntimeError(f"GitHub API failed for {path}: {exc}") from exc
    except URLError as exc:
        raise RuntimeError(f"GitHub network error: {exc}") from exc

def fetch_counts(today):
    start = today - timedelta(days=89)
    repos = []
    for page in range(1,11):
        batch = api(f"/users/{USER}/repos?type=owner&per_page=100&page={page}")
        repos += [r for r in batch if not r.get("private") and not r.get("fork")]
        if len(batch) < 100: break
    counts = Counter()
    for repo in repos:
        seen = set()
        for page in range(1,11):
            url = f"/repos/{repo['full_name']}/commits?since={start.isoformat()}T00%3A00%3A00Z&per_page=100&page={page}"
            commits = api(url)
            for commit in commits:
                sha = commit.get("sha")
                if not sha or sha in seen: continue
                seen.add(sha)
                login = (commit.get("author") or {}).get("login","").lower()
                author = (commit.get("commit") or {}).get("author") or {}
                email = author.get("email","").lower()
                if login != USER and f"{USER}@" not in email and f"+{USER}@" not in email: continue
                day = (author.get("date") or "")[:10]
                if start.isoformat() <= day <= today.isoformat(): counts[day] += 1
            if len(commits) < 100: break
    return counts, len(repos)

def render(counts, repo_count, today):
    start = today - timedelta(days=89)
    days = [today-timedelta(days=90-i) for i in range(91)]
    values = [counts.get(day.isoformat(),0) if day >= start else 0 for day in days]
    total, active = sum(values), sum(x > 0 for x in values)
    weeks = [sum(values[i*7:(i+1)*7]) for i in range(13)]
    maxweek = max(weeks,default=0)
    css = ".mono{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Arial,sans-serif}.sans{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Arial,sans-serif}"
    css += "@media(prefers-color-scheme:dark){"+ "".join(f'[data-fill="{k}"]{{fill:{v}}}[data-stroke="{k}"]{{stroke:{v}}}' for k,v in DARK.items())+"}"
    def fill(k): return f'data-fill="{k}" fill="{LIGHT[k]}"'
    def stroke(k): return f'data-stroke="{k}" stroke="{LIGHT[k]}"'
    p = [
       f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="420" viewBox="0 0 1000 420" role="img" aria-label="{total} public commits over 90 days for {USER}">',
       f'<title>Public GitHub commits — {USER}</title>',
       '<desc>Public authored commits in non-fork owned repositories, by UTC author date. Private repositories, pull requests and other activity are not included.</desc>',
       '<style>'+css+'</style>',
       f'<rect x="2" y="2" width="996" height="416" rx="26" {fill("bg")} {stroke("line")}/>',
       f'<text x="42" y="40" class="mono" font-size="24" font-weight="600" letter-spacing="0" {fill("accent")}>GitHub activity</text>',
       f'<text x="958" y="40" text-anchor="end" class="mono" font-size="11" {fill("muted")}>Last 90 days · UTC</text>',
       f'<line x1="43" y1="54" x2="957" y2="54" {stroke("line")}/>',
       f'<line x1="642" y1="80" x2="642" y2="359" {stroke("line")}/>',
       f'<text x="60" y="87" class="mono" font-size="12" {fill("muted")}>Daily public commits</text>']
    for i,day in enumerate(days):
        col,row = divmod(i,7)
        num=values[i]
        shade="empty" if not num else "a1" if num<=2 else "a2" if num<=9 else "a3" if num<=29 else "a4"
        p.append(f'<rect x="{60+42*col}" y="{108+31*row}" width="32" height="23" rx="4" {fill(shade)}><title>{day.isoformat()}: {num} public commits</title></rect>')
    p += [f'<text x="60" y="337" class="mono" font-size="10.5" {fill("muted")}>Older</text>',
          f'<text x="606" y="337" text-anchor="end" class="mono" font-size="10.5" {fill("muted")}>Recent</text>']
    for i,weekly in enumerate(weeks):
        height=4 if not maxweek else max(4,round(16*weekly/maxweek))
        p.append(f'<rect x="{60+42*i}" y="{365-height}" width="32" height="{height}" rx="2" opacity="{0.3 if weekly==0 else 1}" {fill("accent")}/>')
    for y,label,number in [(117,"Public commits",total),(217,"Active days",active),(317,"Public repositories",repo_count)]:
        p.append(f'<text x="689" y="{y}" class="mono" font-size="11.5" letter-spacing="0" {fill("muted")}>{label}</text>')
        p.append(f'<text x="689" y="{y+51}" class="sans" font-size="48" font-weight="700" {fill("ink")}>{number}</text>')
    p += [f'<line x1="43" y1="385" x2="957" y2="385" {stroke("line")}/>',
          f'<text x="44" y="406" class="mono" font-size="10.7" {fill("muted")}>Public GitHub commits · UTC author date · Updated {today.isoformat()}</text>',
          '</svg>']
    return "\n".join(p)+"\n"

def main():
    today=datetime.now(timezone.utc).date()
    counts,repos=fetch_counts(today)
    DEST.parent.mkdir(parents=True,exist_ok=True)
    DEST.write_text(render(counts,repos,today),encoding="utf-8")
    print(f"Updated {DEST} with {sum(counts.values())} public commits across {repos} repos")

if __name__=="__main__": main()
