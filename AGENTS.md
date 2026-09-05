# Repository Guidelines

## Project Structure & Module Organization

This repository publishes bilingual AI infrastructure reference tables; it has no application runtime.

- `data/<id>.yaml`: source specifications, translations, notes, and citations; one file per category.
- `scripts/generate.py`: validates YAML and renders Markdown using PyYAML.
- `templates/README*.tmpl`: English and Chinese README layouts and tables of contents.
- `README.md`, `README.zh-CN.md`, and `docs/*.md`: generated outputs. Never edit them directly.
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

Follow existing Python conventions: four-space indentation, snake_case functions, and uppercase constants. YAML uses two-space indentation. Use kebab-case category and item IDs, such as `datacenter-gpus`; category IDs should match filenames.

Provide `label` and `label_zh` for fields. Share numbers and units through `specs`; translate prose through `specs_zh`. Quote punctuation-heavy inline YAML values or use block mappings. No formatter or linter is configured.

For a new category, add its YAML, register its ID in `ORDER`, and add a section placeholder and contents entry to both templates before regenerating.

## Data & Citation Requirements

Put source URLs in each item's `sources` list. Prefer vendor datasheets, then product pages, announcements, and reputable technical reporting. Identify precision, dense versus sparse compute, measurement scope, and bandwidth direction. Keep units consistent.

Do not guess unpublished specifications. Use `TBA` for unannounced values, omit inapplicable fields, and label roadmap products `(announced)` with explanatory notes.

## Testing Guidelines

There is no standalone test framework or coverage threshold. Run `--check` before committing; CI runs the same validation. Review generated tables in both languages and manually check contents anchors after title changes. Passing validation does not establish factual accuracy or verify citations.

## Commit & Pull Request Guidelines

History uses short imperative subjects, such as `Add inference engines and local apps table` and `Fix layering: Metal is the CUDA peer, MLX is not`.

Keep changes focused. Include source YAML and regenerated Markdown together. Describe affected tables, explain corrections with source links, reference relevant issues, and report validation results. Follow `CONTRIBUTING.md` for the complete contribution workflow.
