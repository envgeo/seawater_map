# EnvGeo-Seawater Documentation

This directory collects project documents that are too detailed for the top-level README.
Historical and development records are retained when useful, but they are not
release approval or a statement of the stable public scope.

[日本語版](README_Japanese.md)

## Current Documents

- `release_checklist.md` / `release_checklist_Japanese.md`
  Checklist for local testing, Streamlit deployment, GitHub release preparation, and Zenodo/DOI archiving.

- `stable_release_publication_notes.md` / `stable_release_publication_notes_Japanese.md`
  Concise stable-release scope, excluded material, data and private-file rules,
  and the required GitHub Release / Zenodo sequence.

- `code_guide.md` / `code_guide_Japanese.md`
  Concise map of core modules, the stable page set, resource directories, and
  code-documentation conventions.

- `publication_content_review_checklist.md` /
  `publication_content_review_checklist_Japanese.md`
  File-by-file public-content review checklist for the stable repository,
  including code, documents, data, assets, and exclusion checks.

- `sprint3_distribution_design_and_acceptance.md` /
  `sprint3_distribution_design_and_acceptance_Japanese.md`
  Current distribution design and verification record for the 1.3.4 stable
  repository; “Sprint 3” is explained in the document.

- `testing.md` / `testing_Japanese.md`  
  Public-facing explanation of the current pytest suite, its scope, limitations, and planned expansion.

- `streamlit_migration.md` / `streamlit_migration_Japanese.md`
  Local migration log for Python 3.12, Streamlit 1.63, Plotly compatibility, environment comparisons, and visual checks.

- `integrated_visualizer_strategy.md` / `integrated_visualizer_strategy_Japanese.md`
  Development architecture and migration history for individual pages, shared
  user-data upload, and Integrated Visualizer. The Page 90 workflow is outside
  the stable-release scope.

- `development_notes.md` / `development_notes_Japanese.md`
  Historical 1.3.3 development notes: offline-map design, user-data
  architecture, bundled geospatial assets, deferred work, and safe cleanup
  conditions. They are technical history, not the current release checklist.

- `distribution_foundation_audit_and_plan.md` /
  `distribution_foundation_audit_and_plan_Japanese.md`, and
  `wheel_proof_report.md` / `wheel_proof_report_Japanese.md`
  Historical Sprint 2 foundation-audit and local wheel-proof records. They
  explain how the later distribution design was reached; the current 1.3.4
  verification record is `sprint3_distribution_design_and_acceptance*.md`.

- `offline_operation_log.md` / `offline_operation_log_Japanese.md`
  Current offline/degraded-network map behavior, self-contained HTML exports,
  known limitations, and verification scope.

- `manual/` / `manual_Japanese/`  
  Page-by-page bilingual user manuals for the stable public workflows. They are
  the content source for the planned static documentation website and may also
  be reused for laboratory-web guidance.

## Planned Documents

- `joss_checklist.md`  
  Checklist for future JOSS resubmission, including tests, documentation, examples, citation, license, and archival DOI.
