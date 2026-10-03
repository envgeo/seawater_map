# Code Guide

This concise guide maps the stable EnvGeo-Seawater source tree for contributors
and reviewers. It explains responsibilities and boundaries; it is not an API
reference and does not replace in-code docstrings or user manuals.

[日本語版](code_guide_Japanese.md)

For the current publication scope, see
[`stable_release_publication_notes.md`](stable_release_publication_notes.md).

## Core modules

| File | Responsibility | Change with care |
|---|---|---|
| `home.py` | Streamlit entry point and Home tabs: overview, references, manuals, and update history. | Keep both `streamlit run home.py` and the installed entry point working. |
| `envgeo_assets.py` | Resolves paths to read-only bundled resources independently of the current working directory. | Use `asset_path()` only for bundled resources, not private data, output, or writable caches. |
| `envgeo_launcher.py` | Console entry point that starts the installed application with `envgeo-seawater`. | Keep its launch path independent of the caller's working directory. |
| `envgeo_diagnostic_launcher.py` | Console entry point for the local diagnostic tool, `envgeo-seawater-check`. | Keep diagnostics outside normal public Streamlit navigation. |
| `envgeo_utils.py` | Shared dataset loading, normalisation, quality checks, filters, map styles, coastlines, and common exports. | Broad legacy infrastructure: make focused, tested changes and avoid unrelated refactoring. |
| `envgeo_user_data.py` | Session-only browser uploads, column normalisation, quality feedback, and uploaded-marker helpers. | Never silently write uploads to disk or merge them into public reference data. |

## Stable page scripts

| Page | Main purpose | Status / special boundary |
|---|---|---|
| `03_[Interactive]_2Dplus_Visualizer.py` | Interactive 2-D comparison views. | Preserve Plotly Box/Lasso behaviour and the distinction between observations and reference contours. |
| `04_[Interactive]_3D_4D_Visualizer.py` | Interactive 3-D/4-D visualisation. | HTML export is self-contained except for online map tiles. |
| `05_User_Data_Check_Quick_Visualizer.py` | Upload-first quality check and simple 2-D–4-D exploration. | Keep uploaded-marker settings before filtering and retain data-origin distinctions. |
| `31_Salinity-d18O_Relationship.py` | Salinity–δ18O relationships. | Uses shared filtering and optional uploaded overlays. |
| `32_Isotope_Hydrographic_Mapping.py` | Plotly and Cartopy mapping. | Use bundled Natural Earth land; do not reintroduce automatic Natural Earth downloads. |
| `34_T-S_diagram.py` | T–S diagram and approximate σ0 reference contours. | Reference contours are not pointwise density. |
| `35_Custom_Parameter_Plot.py` | Flexible custom-parameter plot. | Preserve common upload/filter behaviour. |
| `37_Depth_Profile.py` | Depth-profile visualisation. | Uses shared filtering and uploaded overlays. |
| `53_Vertical_Section_Visualizer.py` | A–B vertical sections and optional derived GEBCO bathymetry. | Beta; retain offline fallback and explicit scientific limitations. |
| `80_Correlation_Overview.py` | Preserved correlation/exploratory workflow. | Historical hand-written archive page; make only necessary bug, compatibility, safety, or distribution fixes. |

Page 90, Page 91, and Page 99 are deliberately outside this stable repository;
the reasons and boundaries are recorded in the stable publication notes.

## Data and resource directories

| Directory | Contents and rule |
|---|---|
| `dataset/` | Source-cited reference workbooks. Do not alter them without dedicated data and provenance review. |
| `local_data/` | Public zero-value `user_data.xlsx` sample and bilingual instructions. Keep researcher-owned measurements outside the public clone. |
| `coastline/` | Offline coastline CSVs, Natural Earth 50m land shapefile, and provenance. |
| `bathymetry/` | Derived GEBCO grid and its source-only generation helper. Page 53 reads the grid only; the helper is excluded from wheels. |
| `data/` and `data_text/` | Demonstration media, in-app text, references, manuals, and update logs. |
| `docs/` | Release records, historical development material, scientific plans, and bilingual documentation. |
| `test/` | Pytest regression tests. Add focused tests with behavioural changes. |

## Documentation rule of thumb

- Write a short docstring for reusable modules and public helpers: purpose,
  inputs/outputs, and important safety boundary.
- Use code comments for non-obvious intent, scientific assumptions, or
  compatibility constraints; do not comment obvious assignments.
- Use bilingual section headers to mark a meaningful boundary between settings,
  data structures, and related helper functions. Prefer a small number of
  role-based groups over a header for every short assignment or every `def`.
- Put longer explanations, provenance, and release decisions in `docs/`.
- Keep English and Japanese records aligned when a decision affects users,
  reproducibility, release claims, or scientific interpretation.

## Code comment and formatting convention

Apply this convention to active shared code and active stable pages. The
historical Page 80 archive is exempt except for necessary functional, safety,
or distribution fixes.

```python
# =============================================================================
# Major role-based section / 主要な役割区分
# =============================================================================

# -------------------------------------------------------------------
# Related subgroup / 関連する下位区分
# -------------------------------------------------------------------
```

- Use `=` for a module-level area such as configuration, data loading, map
  styling, or reporting; use `-` for a related subgroup or coherent stage in a
  long function.
- Place English first and Japanese second. State the role or reason, not edit
  history; avoid “fixed”, dates, and temporary-development notes.
- Do not number major sections. Short numbered steps inside one non-trivial
  procedure are acceptable when they make the sequence clearer.
- Retain explanations for scientific assumptions, missing-value/gap-row
  preservation, compatibility constraints, provenance boundaries, and
  non-obvious safety handling. Remove confirmed-unused debug output, obsolete
  commented-out code, and duplicate implementation examples.
- Keep ordinary assignments uncommented. Put lengthy rationale, decisions, and
  user-facing explanations in `docs/`.
- Separate formatting-only from behaviour changes where practical; then run
  syntax checks and focused tests appropriate to the risk.
