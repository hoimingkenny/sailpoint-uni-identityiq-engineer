# Identity Security Engineer, IdentityIQ — Study Notes

Personal English learning notes for the SailPoint University path. **The learning path remains incomplete.** Updated 16 November 2026.

## Read the material

- **[IdentityIQ Essentials — Modules 1–6 and Exercise 1](study/courses/02-essentials/notes.md)**: Course Overview, Technical Overview, Functional Elements, Implementation Overview, Product Architecture and Installation. About 4,600 words with 49 original English handout page illustrations. Modules 7–33 are pending.
- **[IdentityIQ Introduction — twelve topics](study/courses/01-introduction/notes.md)**: detailed English explanations with 62 saved original inline images; five demonstrations remain untranscribed.
- **[Complete verified course outline](inventory/learning-path.md)** and **[coverage / missing-material report](study/coverage-report.md)**.

After cloning or downloading the repository, open **[the searchable offline book](study/index.html)**. It contains the actual notes from both courses in reading order. Select an illustration to open its full local image. The separate **[Essentials reader](study/courses/02-essentials/index.html)** includes a status table for all 33 numbered modules.

## Current coverage

The path lists five teaching courses with a displayed duration of 60 hours 30 minutes, plus two certification exams. A whole-path internal lesson count is not yet verified.

Essentials notes draw on accessible video caption-search results, the provided presentation handout, and the relevant exercise-guide pages. The original 461-page slide PDF and 257-page exercise guide are saved under [Essentials handouts](study/courses/02-essentials/handouts/). Saving the complete handouts does not mean their later modules have been rewritten. The source guide identifies IdentityIQ 8.2b; original version-specific examples are explained as course context.

There are **111 image files**: 62 Introduction inline originals and 49 Essentials PDF-page renders. Original English text in the images is preserved. Full videos, changing video frames, interactive checks and some linked resources remain missing. No VM operations or live IdentityIQ changes were performed; exercise steps are study instructions.

Rules / Scripts / API and Custom Reports remain at outline-only coverage. Advanced Provisioning and Workflows requires completion of an accepted Essentials course before registration. Certification exam content is excluded.

## Repository structure

- `study/` — searchable offline HTML, English Markdown, illustrations, original handouts and coverage records.
- `inventory/` — verified path and module structure.
- `capture-progress.json` — explicit progress and next module: **Essentials 7 — Creating Identity Cubes**.
- `tools/build_reader.py` — rebuilds the reader, coverage CSV and progress report; verifies illustration hashes and references.

Rebuild with Python 3: `python3 tools/build_reader.py`. No external packages or internet connection are required to read or rebuild the saved notes.

The prose is paraphrased and follows course order. Original materials belong to their respective owners. This is a personal study repository, not an official SailPoint publication. No access controls or DRM were bypassed.
