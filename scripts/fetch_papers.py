#!/usr/bin/env python3
"""Fetch metadata for a curated set of Indic ASR papers via OpenAlex.

Writes docs/data/papers.json. Intended to run in GitHub Actions (compute).
"""
import json, time, urllib.request, urllib.parse
from pathlib import Path

IDS = [
    "2111.03945", "2104.00235", "2106.01400", "2107.07402",
    "2208.11761", "2208.12666", "2212.04356", "2303.01037",
    "2305.15386", "2305.15760", "2305.13516", "2308.11596",
    "2309.13876", "2403.01926", "2409.05356", "2408.11440",
    "2506.09653", "2511.09690", "2508.06280", "2604.19151",
    "2607.23808", "2605.20712", "2605.03073", "2606.02548",
    "2606.09345", "2606.09335", "2606.17662", "2608.08235",
]

def fetch_one(aid):
    doi = "10.48550/arxiv." + aid
    url = "https://api.openalex.org/works/doi:" + urllib.parse.quote(doi, safe="")
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            d = json.load(r)
    except Exception as e:
        return {"id": aid, "error": str(e)}
    authors = [a.get("author", {}).get("display_name") for a in d.get("authorships", [])]
    return {
        "id": aid,
        "doi": d.get("doi"),
        "title": d.get("title"),
        "published": d.get("publication_date"),
        "cited_by_count": d.get("cited_by_count"),
        "authors": authors[:6],
        "openalex": d.get("id"),
    }

def main():
    out = []
    for aid in IDS:
        rec = fetch_one(aid)
        out.append(rec)
        print("OK" if "title" in rec else "FAIL", aid, rec.get("title", rec.get("error", ""))[:60])
        time.sleep(0.5)
    Path("docs/data").mkdir(parents=True, exist_ok=True)
    Path("docs/data/papers.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print("wrote", len(out), "records")

if __name__ == "__main__":
    main()
