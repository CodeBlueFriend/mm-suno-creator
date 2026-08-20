---
name: mm-suno-creator
description: Turn song ideas into structured Suno creation packs with singable Chinese, English, or bilingual lyrics; concise and standard Style prompts; exclusions; parameter guidance; duration budgets; tag explanations; conflict checks; and next-generation iteration advice. Use for Suno songwriting, lyric revision, style/tag lookup, prompt assembly, vocal or duration planning, and preflight review. Do not use for finished-audio mixing, source detection, watermark removal, or operating a Suno account.
---

# MM Suno Creator

Convert the request into an executable creation pack. Prefer concrete musical attributes over named-artist imitation.

## Workflow

1. Build a brief covering theme, language, genre axis, emotional arc, vocal, duration, hook, use case, and exclusions. Adopt reversible defaults; ask only when a missing choice materially changes the song.
2. Design the section structure and time budget before writing or revising lyrics.
3. Make each language singable on its own. Do not make bilingual lyrics a word-for-word translation.
4. Assemble one primary genre, at most two secondary directions, then rhythm, vocal, instrumentation, production, mood, and exclusions.
5. Produce concise and standard Style variants. Keep experimental choices isolated from the stable version.
6. Explain parameter directions from the user's goal; do not present mutable platform behavior as permanent fact.
7. Run the bundled scripts for tag lookup, Style linting, lyric analysis, and pack rendering when their inputs are available.
8. Review duration, section arrival, vocal range, pronunciation, tag conflicts, exclusions, copyright/style risk, and the next single-variable iteration.

## Required output

Return a brief, paste-ready lyrics, concise Style, standard Style, exclusions, parameter guidance with reasons, section time budget, tag explanations, risks, and a controlled next-round plan.

## Resources

- Read [references/songwriting.md](references/songwriting.md) for lyric and structure rules.
- Read [references/tag-taxonomy.md](references/tag-taxonomy.md) for tag selection and evidence rules.
- Read [references/platform-and-rights.md](references/platform-and-rights.md) for mutable Suno behavior and style/copyright boundaries.
- Run `python scripts/query_tags.py <query>` to search the curated seed dictionary.
- Run `python scripts/lint_style_prompt.py "<style>"` to find length, repetition, and known conflicts.
- Run `python scripts/analyze_lyrics.py <lyrics-file>` to estimate section and duration properties.
- Run `python scripts/build_generation_pack.py <input.json> --output <pack.md>` to render the standard package.

Treat dictionary support states as evidence labels, not guarantees. Never invent official support or claim that a prompt will force deterministic output.
