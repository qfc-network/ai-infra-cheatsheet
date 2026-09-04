# Contributing

Thanks for helping keep the numbers honest. Everything in `README.md`,
`README.zh-CN.md` and `docs/` is **generated** — edit the YAML in `data/`, never
the Markdown.

## Workflow

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/generate.py          # regenerate Markdown
python scripts/generate.py --check  # what CI runs
```

Commit the changed YAML **and** the regenerated Markdown in the same PR. CI
fails if they drift apart.

## Rules for spec data

1. **Cite a source.** Every item carries a `sources:` list. Prefer, in order:
   NVIDIA datasheet (PDF) → NVIDIA product page → NVIDIA press release / GTC
   keynote → reputable technical press. No forum posts or rumors.
2. **Say which number it is.** Dense vs sparse, per-GPU vs per-node vs per-rack,
   uni- vs bidirectional. If the field label does not already pin it down, put
   it in the value: `9 PFLOPS (dense)`.
3. **Keep units consistent** with the rest of the column (`GB/s` vs `TB/s`,
   `Gbit/s` for network ports).
4. **Unknown is fine.** Use `TBA` for unannounced and leave the key out if the
   parameter does not apply — the generator renders `-`.
5. **Roadmap parts** must be labelled `(announced)` in the item name and noted in
   the category `notes`.
6. **No marketing adjectives.** "up to", "class" and "~" are allowed when the
   source itself is approximate.

## Adding a field

Add it to the category's `fields:` list with both `label` and `label_zh`, then
fill it in for every item. Items missing the key render as `-`.

## Adding a category

1. Create `data/<id>.yaml` following an existing file.
2. Add `<id>` to `ORDER` in `scripts/generate.py`.
3. Add `{{section:<id>}}` plus a table-of-contents entry to both templates in
   `templates/`.
4. Run the generator.

## Chinese text

Values are usually language-neutral (numbers and units) and are shared. Only
prose values need a translation — add them under `specs_zh:` for that item, and
they override `specs:` in the Chinese output.
