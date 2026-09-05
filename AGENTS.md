# Repository Guidelines

This repository publishes bilingual AI infrastructure reference tables; it has no
application runtime. The deliverable is correct, sourced data rendered into
Markdown.

This file is the single source of guidance for coding agents. `CLAUDE.md` points
here rather than repeating it.

## Project Structure & Module Organization

```
data/*.yaml  ──►  scripts/generate.py  ──►  README.md, README.zh-CN.md, docs/*.md
templates/*.tmpl ──┘
```

- `data/<id>.yaml`: source specifications, translations, notes, and citations; one file per category.
- `scripts/generate.py`: validates YAML and renders Markdown using PyYAML.
- `templates/README*.tmpl`: English and Chinese README layouts and tables of contents.
- `README.md`, `README.zh-CN.md`, and `docs/*.md`: generated outputs. Never edit them directly — a manual edit is silently reverted on the next generate and fails CI in between.
- `.github/workflows/generate.yml`: CI validation. No dedicated test or asset directories exist.

## Build, Test, and Development Commands

Use Python 3.12 to match CI:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/generate.py          # Regenerate both languages
python scripts/generate.py --check  # Validate data and detect stale outputs
```

## Coding Style & Naming Conventions

Follow existing Python conventions: four-space indentation, snake_case functions, and uppercase constants. YAML uses two-space indentation. Use kebab-case category and item IDs, such as `datacenter-gpus`; category IDs should match filenames. No formatter or linter is configured.

## Adding a Category

Three places must change together. Adding the YAML alone does nothing and breaks
the build — the generator errors if a data file is missing from `ORDER` or vice
versa.

1. `data/<id>.yaml`
2. `ORDER` in `scripts/generate.py`. Its comment groups mirror the README's `##` sections.
3. Both templates: a `{{section3:<id>}}` placeholder **and** a table-of-contents entry. An unresolved `{{...}}` placeholder is a hard error.

## Category Schema

```yaml
id: dgx-systems              # must equal the filename stem
title: DGX Systems
title_zh: DGX 整机
summary: >-                  # optional; summary_zh alongside
orientation: columns         # or rows
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

- Provide `label` and `label_zh` for every field.
- `orientation: columns` puts items in columns and fields in rows. Readable up to about seven items; past that use `rows`.
- Share numbers and units through `specs`; only prose values need a `specs_zh` entry, and anything absent falls back to `specs`.
- A missing field key renders as `-`. An **unknown** key is a hard error, which is how typos get caught.
- `{{table_count}}` in the templates resolves to `len(ORDER)`, so the README badge cannot go stale.

### YAML traps this repo has already hit

Inline mappings (`specs: {a: 1, b: 2}`) silently mis-parse on unquoted `,`, `?`
and `:` inside a value. Quote the value or use block style. The validator catches
the result, but its error message points at the wrong key.

## Data & Citation Requirements

These rules are the point of the project, not bureaucracy. `CONTRIBUTING.md` is
the public version.

1. **Every value needs a source**, in order: vendor datasheet → product page → announcement or keynote → reputable technical reporting. Put the URL in the item's `sources`.
2. **"Not officially published" beats a guess.** Where a vendor never released a figure, the cell says so. The Huawei 910B/910C rows are deliberately mostly empty for this reason; do not fill them from analyst estimates. Use `TBA` for unannounced values, omit inapplicable fields, and label roadmap products `(announced)`.
3. **State which number it is.** Dense vs sparse, per-GPU vs per-node vs per-rack, bandwidth direction. Keep units consistent within a column.
4. **Vendor headline figures are not comparable across vendors** and the tables must say so. NVIDIA moved from quoting FP8 to FP4, AMD quotes MXFP4, Intel quotes INT8 TOPS, Apple publishes nothing equivalent.
5. Anchors in the hand-written tables of contents are not validated by the generator. After changing any title, check every `](#...)` link resolves in both languages.

## Fetching Vendor Specs

`WebFetch` times out on `amd.com` and returns unusable bytes for PDFs. What
works: `curl` the PDF with a browser User-Agent, then `pdftotext` — plain output
for label/value pairs, `-layout` for tables. This is how the MI350X, MI355X and
Intel Arc Pro B70 figures were sourced. `docs.nvidia.com` and
`rocm.docs.amd.com` respond fine to `WebFetch`.

## Testing Guidelines

There is no standalone test framework or coverage threshold. `--check` is the
test: it validates every YAML file and diffs the generated Markdown against what
is committed. Run it before committing; CI runs the same validation. Review
generated tables in both languages. Passing validation does not establish factual
accuracy or verify citations.

## Commit & Pull Request Guidelines

History uses short imperative subjects, such as `Add inference engines and local apps table` and `Fix layering: Metal is the CUDA peer, MLX is not`.

Keep changes focused. Include source YAML and regenerated Markdown together. Describe affected tables, explain corrections with source links, reference relevant issues, and report validation results. Follow `CONTRIBUTING.md` for the complete contribution workflow.

## Companion Repository

[`qfc-network/ai-infra`](https://github.com/qfc-network/ai-infra) holds prose
deep-dives on the papers and systems (FlashAttention, PagedAttention, GQA,
NVLink). That repo explains mechanisms; this one holds numbers. Several of its
pages (`foundational/blackwell-b200`, `hopper-h100`, `gpu-interconnect`) restate
specs that live here — a known drift risk, deliberately left alone so far.
