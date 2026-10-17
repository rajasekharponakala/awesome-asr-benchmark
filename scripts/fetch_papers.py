#!/usr/bin/env python3
"""Fetch arXiv metadata for a curated set of Indic ASR papers.

Writes docs/data/papers.json. Intended to run in GitHub Actions (compute).
"""
import json, time, urllib.request, urllib.parse, xml.etree.ElementTree as ET
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

NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

def fetch_one(aid, retries=3):
    url = "https://export.arxiv.org/api/query?id_list=" + aid
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                data = r.read().decode("utf-8")
            if "Rate exceeded" in data:
                time.sleep(10 * (attempt + 1))
                continue
            root = ET.fromstring(data)
            entry = root.find("atom:entry", NS)
            if entry is None:
                return None
            title = entry.findtext("atom:title", default="", namespaces=NS).strip().replace("\n", " ")
            published = entry.findtext("atom:published", default="", namespaces=NS)
            summary = entry.findtext("atom:summary", default="", namespaces=NS).strip().replace("\n", " ")
            authors = [a.findtext("atom:name", default="", namespaces=NS) for a in entry.findall("atom:author", NS)]
            return {"id": aid, "title": title, "published": published, "summary": summary[:400], "authors": authors}
        except Exception as e:
            time.sleep(5 * (attempt + 1))
    return None

def main():
    out = []
    for aid in IDS:
        rec = fetch_one(aid)
        if rec:
            out.append(rec)
            print("OK", aid, rec["title"][:60])
        else:
            print("FAIL", aid)
        time.sleep(5)
    Path("docs/data").mkdir(parents=True, exist_ok=True)
    Path("docs/data/papers.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print("wrote", len(out), "records")

if __name__ == "__main__":
    main()
