# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A bilingual (EN / zh-CN) reference of AI hardware spec tables — NVIDIA, AMD,
Intel, Apple, Huawei — plus inference software and VRAM sizing math. There is no
application here; the deliverable is correct, sourced data rendered into
Markdown.

## Commands

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python scripts/generate.py           # regenerate all Markdown from data/
python scripts/generate.py --check   # validate + fail if Markdown is stale (what CI runs)
```

There is no test suite. `--check` is the test: it validates every YAML file and
diffs the generated Markdown against what is committed. Run it before every
commit; CI (`.github/workflows/generate.yml`) runs exactly this on push and PR.

## Architecture

Single-direction pipeline, no runtime:

```
data/*.yaml  ──►  scripts/generate.py  ──►  README.md, README.zh-CN.md, docs/*.md
templates/*.tmpl ──┘
```

- **`data/<id>.yaml`** — one file per table. This is the only place to edit data.
- **`scripts/generate.py`** — validates, renders, writes. ~240 lines, stdlib + PyYAML.
- **`templates/README.md.tmpl`, `templates/README.zh-CN.md.tmpl`** — page skeleton
  with `{{section3:<id>}}` placeholders, prose sections, and the table of contents.
- **`README.md`, `README.zh-CN.md`, `docs/`** — **generated. Never hand-edit.**
  A manual edit is silently reverted on the next generate and fails CI in between.

### The three coupled places when adding a table

Adding `data/foo.yaml` alone does nothing and breaks the build. All three must
change together:

1. `data/foo.yaml`
2. `ORDER` in `scripts/generate.py` — the generator errors if a data file is
   missing from `ORDER` or vice versa. Its comment groups mirror the README's
   `##` sections.
3. Both templates — a `{{section3:foo}}` placeholder **and** a table-of-contents
   entry. An unresolved `{{...}}` placeholder is a hard error.

### Category schema

```yaml
id: dgx-systems              # must equal the filename stem
title: DGX Systems
title_zh: DGX 整机
summary: >-                  # optional; summary_zh alongside
orientation: columns         # or rows — see below
fields:
  - {key: architecture, label: Architecture, label_zh: 架构}
  - {key: fp4,          label: FP4,          label_zh: FP4}
items:
  - id: dgx-h100
    name: DGX H100
    specs:      {architecture: Hopper, fp4: no native FP4}   # keyed by field key
    specs_zh:   {fp4: 无原生 FP4}            # optional per-value zh override
    sources:    [https://...]              # rendered on the docs/ page
notes:      [...]            # rendered as a blockquote under the table
notes_zh:   [...]
```

- `orientation: columns` puts items in columns and fields in rows (the layout of
  the reference tables). Readable up to ~7 items; past that use `rows`.
- Numbers and units are shared between languages. Only prose values need a
  `specs_zh` entry; anything absent falls back to `specs`.
- A missing field key renders as `-`. An **unknown** key is a hard error, which
  is how typos get caught.
- `{{table_count}}` in the templates resolves to `len(ORDER)` so the README badge
  cannot go stale.

### YAML traps this repo has already hit

Inline mappings (`specs: {a: 1, b: 2}`) silently mis-parse on unquoted `,`, `?`
and `:` inside a value. Quote the value or use block style. The validator catches
the result, but the error message points at the wrong key.

## Data rules

These are the point of the project, not bureaucracy. `CONTRIBUTING.md` is the
public version.

1. **Every value needs a source**, in order: vendor datasheet → product page →
   press release or keynote → reputable technical press. Put the URL in the
   item's `sources`.
2. **"Not officially published" beats a guess.** Where a vendor never released a
   figure, the cell says so. The Huawei 910B/910C rows are deliberately mostly
   empty for this reason; do not fill them from analyst estimates.
3. **State which number it is.** Dense vs sparse, per-GPU vs per-node vs
   per-rack. Vendors quote different precisions each generation (NVIDIA moved
   FP8 → FP4, AMD quotes MXFP4, Intel quotes INT8 TOPS, Apple publishes nothing
   comparable), so headline figures are not comparable across vendors and the
   tables must say so.
4. Anchors in the hand-written table of contents are not validated by the
   generator. After changing any title, check every `](#...)` link resolves.

## Fetching vendor specs

`WebFetch` times out on `amd.com` and returns unusable bytes for PDFs. What
works: `curl` the PDF with a browser User-Agent into the scratchpad, then
`pdftotext` (plain for label/value pairs, `-layout` for tables). This is how the
MI350X/MI355X and Intel Arc Pro B70 figures were sourced. `docs.nvidia.com` and
`rocm.docs.amd.com` respond fine to `WebFetch`.

## Companion repo

[`qfc-network/ai-infra`](https://github.com/qfc-network/ai-infra) holds prose
deep-dives on the papers and systems (FlashAttention, PagedAttention, GQA,
NVLink). That repo explains mechanisms; this one holds numbers. Several of its
pages (`foundational/blackwell-b200`, `hopper-h100`, `gpu-interconnect`) restate
specs that live here — a known drift risk, deliberately left alone so far.
