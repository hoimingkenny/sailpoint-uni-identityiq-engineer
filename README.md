# Identity Security Engineer, IdentityIQ — Study Notes

Personal English learning material for the SailPoint University path. Updated 16 November 2026. **Essentials notes cover all 33 numbered modules, and Rules / Scripts / API notes cover all eight internal topics. The broader Engineer learning path remains incomplete.**

## Read the learning material

- **[Rules, Scripts, and API — all eight topic notes](study/courses/03-rules-scripts-api/notes.md)**: BeanShell, API navigation, SailPointContext, objects, extension patterns and best practices, with 42 original images and nine saved demonstration videos.
- **[Rules / Scripts / API exercise companion](study/courses/03-rules-scripts-api/practice-companion.md)**: rewritten instructions and all 37 original guide pages.
- **[IdentityIQ Essentials — all 33 module notes](study/courses/02-essentials/notes.md)**, in course order, with original English slide illustrations and links to related exercises.
- **[Essentials practice companion](study/courses/02-essentials/practice-companion.md)**, with 28 exercise/reference sections and all 257 original guide pages.
- **[IdentityIQ Introduction — twelve topics](study/courses/01-introduction/notes.md)**, with 62 original inline images.
- **[Source depth and missing material](study/coverage-report.md)** and the **[verified learning-path outline](inventory/learning-path.md)**.

After cloning or downloading the repository, open **[the searchable offline book](study/index.html)**. The **[Essentials reader](study/courses/02-essentials/index.html)** includes a linked contents list and source table for every numbered module. Each module is also available separately under [Essentials modules](study/courses/02-essentials/modules/). Select an illustration to open its full local image.

## What is included

Rules / Scripts / API was read through all eight written topics. All four workflow-carousel panels and all three performance tabs are expanded. Its 79 image files comprise 42 inline originals and 37 exercise-guide page renders. Nine original MP4 demonstrations are embedded in the offline HTML reader. They are preserved for playback but are not fully transcribed or reviewed frame by frame; the video-led Object Model chapter remains a conceptual companion to those saved demonstrations. The original exercise PDF and artifact ZIP are included; no artifact was executed.

Essentials contains substantive rewritten explanations for **Modules 1–33**, with **429 nonblank original presentation-page illustrations**. The separate practice companion retains **all 257 original exercise-guide pages**, including diagrams, screenshots, settings, exercise prompts, reference tables and appendix procedures. There are **686 Essentials image files** and **827 image files across the three courses**, plus nine saved Rules / Scripts / API videos.

The original **461-page slide PDF** and **257-page exercise guide** remain unchanged under [Essentials handouts](study/courses/02-essentials/handouts/). Thirty-two blank presentation separator pages are omitted from the reading flow but retained in the source PDF. Original English labels and visual content are preserved inside the page illustrations.

The guide identifies IdentityIQ 8.2b / 2021; some slide examples use 8.1 and 2020 material. Version-specific limits, platform lists and example settings are explained as historical course content rather than a current support matrix.

## Coverage limits

- **Modules 1–7:** accessible video caption-search explanations were reviewed alongside the handouts.
- **Modules 8–33:** notes are supported by their official slides and related exercise-guide material; full video narration remains unreviewed.
- **Audiovisual gaps:** original videos, animations, every changing video frame and interactive knowledge-check execution are not archived. Page-level illustration coverage does not establish all video graphics were captured.
- **Practice:** original pages and rewritten summaries are included. Except for the detailed Exercise 1 rewrite, every low-level field/command has not been rephrased line by line. No VM operations, live configuration changes, access reviews or assessment attempts were performed.
- **Other resources:** the separate VM-access lesson, My lab interface, external linked references, current support matrices and software downloads are not comprehensively archived. Separate Answer Key PDFs and supplied solution files were not used to generate the notes. The retained original Rules / Scripts / API artifact ZIP includes its supplied config and solutions directories.

Custom Reports remains outline-only. Advanced Provisioning and Workflows was gated on accepted Essentials completion during the prior inspection. Compiling notes does not complete that LMS prerequisite. The whole path lists five teaching courses (60 hours 30 minutes displayed) and two separate certification exam entries; the full internal lesson total is still unverified.

## Rebuild and evidence

`python3 tools/build_reader.py` rebuilds the offline readers, per-module pages, coverage CSV and progress report using standard Python 3. It also verifies the hashes and references for all 827 retained images and the nine saved demonstration videos. No external packages or network connection are required to read or rebuild the saved book.

- `inventory/` — verified course/module structure and source basis.
- `study/lesson-coverage.csv` — status for twelve Introduction topics, all 33 Essentials modules and eight Rules / Scripts / API topics.
- `study/courses/02-essentials/coverage.json` — exact source, version, caption, media and practice limitations.
- `capture-progress.json` — separates completed numbered-module notes from pending audiovisual review and other courses.

The prose is paraphrased. Original materials belong to their respective owners. This personal study book is not an official SailPoint publication. No access controls or DRM were bypassed, and no certification exam questions or answers are included.
