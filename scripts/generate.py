#!/usr/bin/env python3
"""Render the Markdown tables in README.md / README.zh-CN.md / docs from data/*.yaml.

Usage:
    python scripts/generate.py           # write files
    python scripts/generate.py --check   # exit 1 if anything is out of date
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
TEMPLATE_DIR = ROOT / "templates"
DOCS_DIR = ROOT / "docs"

LANGS = {
    "en": {"readme": "README.md", "template": "README.md.tmpl", "doc_suffix": ".md"},
    "zh": {"readme": "README.zh-CN.md", "template": "README.zh-CN.md.tmpl", "doc_suffix": ".zh-CN.md"},
}

STRINGS = {
    "en": {"sources": "Sources", "notes": "Notes", "back": "Back to index", "missing": "-"},
    "zh": {"sources": "资料来源", "notes": "说明", "back": "返回目录", "missing": "-"},
}

# Order in which categories appear in the README.
ORDER = [
    # Desktop / local
    "local-systems",
    "consumer-gpus",
    "radeon-gpus",
    "intel-local-gpus",
    # NVIDIA data center
    "dgx-systems",
    "datacenter-gpus",
    "superchips",
    "rack-scale",
    "interconnect",
    "networking",
    "roadmap",
    # AMD
    "amd-gpus",
    "amd-systems",
    # Intel
    "intel-accelerators",
    # China
    "ascend",
    "ascend-superpods",
    "china-other",
    # Cross-vendor
    "head-to-head",
    "local-options",
    # Sizing math
    "quantization",
    "kv-cache",
]


class DataError(Exception):
    pass


def load_categories() -> dict:
    cats = {}
    for path in sorted(DATA_DIR.glob("*.yaml")):
        with path.open(encoding="utf-8") as fh:
            cat = yaml.safe_load(fh)
        if not isinstance(cat, dict):
            raise DataError(f"{path.name}: top level must be a mapping")
        cat["_path"] = path
        validate(cat)
        cats[cat["id"]] = cat
    unknown = set(cats) - set(ORDER)
    if unknown:
        raise DataError(f"categories missing from ORDER in generate.py: {sorted(unknown)}")
    missing = set(ORDER) - set(cats)
    if missing:
        raise DataError(f"ORDER lists categories with no data file: {sorted(missing)}")
    return cats


def validate(cat: dict) -> None:
    name = cat.get("_path", "?")
    for key in ("id", "title", "title_zh", "fields", "items"):
        if not cat.get(key):
            raise DataError(f"{name}: missing required key '{key}'")
    if cat.get("orientation", "columns") not in ("columns", "rows"):
        raise DataError(f"{name}: orientation must be 'columns' or 'rows'")
    field_keys = []
    for field in cat["fields"]:
        for key in ("key", "label", "label_zh"):
            if key not in field:
                raise DataError(f"{name}: field {field} missing '{key}'")
        field_keys.append(field["key"])
    if len(set(field_keys)) != len(field_keys):
        raise DataError(f"{name}: duplicate field keys")
    for bucket in ("notes", "notes_zh"):
        notes = cat.get(bucket)
        if notes is None:
            continue
        if not isinstance(notes, list) or not all(isinstance(n, str) for n in notes):
            raise DataError(f"{name}: '{bucket}' must be a list of strings")
    seen = set()
    for item in cat["items"]:
        if not isinstance(item, dict):
            raise DataError(f"{name}: items must be mappings, got {item!r}")
        if "id" not in item or "name" not in item:
            raise DataError(f"{name}: every item needs 'id' and 'name'")
        if item["id"] in seen:
            raise DataError(f"{name}: duplicate item id '{item['id']}'")
        seen.add(item["id"])
        for bucket in ("specs", "specs_zh"):
            for key in item.get(bucket) or {}:
                if key not in field_keys:
                    raise DataError(f"{name}: item '{item['id']}' has unknown {bucket} key '{key}'")


def cell(item: dict, key: str, lang: str) -> str:
    specs = item.get("specs") or {}
    value = (item.get("specs_zh") or {}).get(key) if lang == "zh" else None
    if value is None:
        value = specs.get(key)
    if value is None or value == "":
        return STRINGS[lang]["missing"]
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def render_table(cat: dict, lang: str) -> str:
    label = (lambda f: f["label_zh"]) if lang == "zh" else (lambda f: f["label"])
    fields, items = cat["fields"], cat["items"]
    if cat.get("orientation", "columns") == "columns":
        header = ["Parameter" if lang == "en" else "参数"] + [i["name"] for i in items]
        rows = [[label(f)] + [cell(i, f["key"], lang) for i in items] for f in fields]
    else:
        header = ["Name" if lang == "en" else "名称"] + [label(f) for f in fields]
        rows = [[i["name"]] + [cell(i, f["key"], lang) for f in fields] for i in items]
    out = ["| " + " | ".join(header) + " |",
           "|" + "|".join(["---"] * len(header)) + "|"]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(out)


def render_notes(cat: dict, lang: str) -> str:
    notes = cat.get("notes_zh" if lang == "zh" else "notes") or cat.get("notes") or []
    if not notes:
        return ""
    return "\n".join(f"> - {n.strip()}" for n in notes)


def render_section(cat: dict, lang: str, heading: str = "##") -> str:
    title = cat["title_zh"] if lang == "zh" else cat["title"]
    summary = cat.get("summary_zh" if lang == "zh" else "summary") or ""
    parts = [f"{heading} {title}", ""]
    if summary:
        parts += [summary.strip(), ""]
    parts += [render_table(cat, lang), ""]
    notes = render_notes(cat, lang)
    if notes:
        parts += [notes, ""]
    return "\n".join(parts).rstrip() + "\n"


def render_doc(cat: dict, lang: str) -> str:
    title = cat["title_zh"] if lang == "zh" else cat["title"]
    s = STRINGS[lang]
    other = "README.zh-CN.md" if lang == "en" else "README.md"
    parts = [f"# {title}", "", render_section(cat, lang, heading="##").split("\n", 2)[2].lstrip()]
    links = []
    for item in cat["items"]:
        for src in item.get("sources") or []:
            entry = f"- [{item['name']}]({src})"
            if entry not in links:
                links.append(entry)
    if links:
        parts += ["", f"## {s['sources']}", ""] + links
    parts += ["", "---", "", f"[{s['back']}](../{other})", ""]
    return "\n".join(parts)


def render_readme(cats: dict, lang: str) -> str:
    template = (TEMPLATE_DIR / LANGS[lang]["template"]).read_text(encoding="utf-8")
    for cid in ORDER:
        cat = cats[cid]
        template = template.replace(f"{{{{section:{cid}}}}}", render_section(cat, lang).rstrip())
        template = template.replace(f"{{{{section3:{cid}}}}}", render_section(cat, lang, heading="###").rstrip())
        template = template.replace(f"{{{{table:{cid}}}}}", render_table(cat, lang))
    if "{{" in template:
        leftover = template[template.index("{{"): template.index("{{") + 40]
        raise DataError(f"unresolved placeholder in {LANGS[lang]['template']}: {leftover!r}")
    return template


def write(path: Path, content: str, check: bool, stale: list) -> None:
    current = path.read_text(encoding="utf-8") if path.exists() else None
    if current == content:
        return
    if check:
        stale.append(path.relative_to(ROOT))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if generated files are out of date")
    args = ap.parse_args()
    stale: list = []
    try:
        cats = load_categories()
        for lang, cfg in LANGS.items():
            write(ROOT / cfg["readme"], render_readme(cats, lang), args.check, stale)
            for cid in ORDER:
                write(DOCS_DIR / f"{cid}{cfg['doc_suffix']}", render_doc(cats[cid], lang), args.check, stale)
    except DataError as exc:
        print(f"data error: {exc}", file=sys.stderr)
        return 1
    if stale:
        print("out of date: " + ", ".join(str(p) for p in stale), file=sys.stderr)
        print("run: python scripts/generate.py", file=sys.stderr)
        return 1
    if args.check:
        print("all generated files are up to date")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
