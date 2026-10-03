# EnvGeo-Seawater Release Checklist

Use this checklist before uploading a test site, updating GitHub, creating a release, or archiving a version with Zenodo.

[日本語版](release_checklist_Japanese.md)

`seawater_map` is the formal stable-release repository. Use this checklist for
the tagged GitHub Release, Zenodo archive, and JOSS-facing software record.

## 1. Local Environment

### Stable release 1.3.4 (2026-10-03)

- [x] Python 3.12 / Streamlit 1.63 / Plotly 5.24 environment used for the
  final test run.
- [x] Stable CI run #5 (2026-10-03) completed on Python 3.10 and 3.12:
  tests, wheel build, isolated-wheel installation, and one wheel artifact per
  Python version all succeeded.

### Earlier manual smoke evidence (repeat after the release commit)

The following exploratory checks were completed during the release-candidate
review. They provide useful evidence, but do **not** replace the final manual
check against the committed stable release and its deployment.

- [x] Home opened, and the local-only `99_Environment_Check.py` page was absent
      from the public sidebar.
- [x] Mapping, T–S Diagram, and Depth Profile opened without an application
      error; data selection and `Apply settings` updated the displayed result.
- [x] A Mapping background tile loaded successfully.
- [x] No application error screen was present. A static public-file and wheel
      audit separately checked for absolute local paths and credential-like
      values.

- [ ] Confirm the intended Python environment is active.
- [ ] Confirm one of the tested baselines is active: Python 3.10.15 / Streamlit 1.42 or Python 3.12.14 / Streamlit 1.63, both with Plotly 5.24.
- [ ] Confirm `requirements.txt` matches the tested environment.
- [ ] Run the local environment checker if needed:

```bash
streamlit run tools/env_check_streamlit.py
```

- [ ] Export the environment report as CSV or PDF when useful for release records.

## 2. Basic App Startup

- [ ] Start the app locally:

```bash
streamlit run home.py
```

- [ ] Confirm `home.py` opens successfully.
- [ ] Confirm the app version is shown as `1.3.4 (2026-09-28)`.
- [ ] Confirm the Home tabs load: Main, About, Data Sources, Manual, Update History, and Japanese information where applicable.

## 3. Sidebar And Filtering

- [ ] Confirm `Data filtering` appears in the sidebar.
- [ ] Confirm the note about clicking `Apply settings` is visible.
- [ ] Confirm `Area filter preset` changes the initial Longitude / Latitude range.
- [ ] Confirm manual Longitude / Latitude slider adjustment still works after choosing an area preset.
- [ ] Confirm `Apply settings` updates figures after changing filters.
- [ ] Confirm `Details and statistics of filtered data` opens and exports CSV correctly.

## 4. Main Visualization Pages

Open each page and perform a light visual check.

- [ ] `03_[Interactive]_2Dplus_Visualizer.py`
- [ ] `04_[Interactive]_3D_4D_Visualizer.py`
- [ ] `31_Salinity-d18O_Relationship.py`
- [ ] `32_Isotope_Hydrographic_Mapping.py`
- [ ] `34_T-S_diagram.py`
- [ ] `35_Custom_Parameter_Plot.py`
- [ ] `37_Depth_Profile.py`
- [ ] `05_User_Data_Check_Quick_Visualizer.py`
- [ ] `53_Vertical_Section_Visualizer.py`
- [ ] `80_Correlation_Overview.py`

For each page:

- [ ] Data source selection works.
- [ ] Filtering works after `Apply settings`.
- [ ] Main figures render without errors.
- [ ] Captions, help buttons, and labels are understandable.
- [ ] `Sampling Location Map` renders correctly where present.
- [ ] `Map controls` and `Map style` work where present.
- [ ] No obvious text overlap or layout break appears.

## 5. Figure Export

- [ ] Confirm 2D Matplotlib figures show `Download image` below the figure.
- [ ] Confirm downloaded PNG files open correctly.
- [ ] Confirm figure titles fit within downloaded images, especially Depth Profile.
- [ ] Confirm file names are reasonable and do not contain unsafe characters.
- [ ] Decide whether Plotly figures and maps should rely on the Plotly modebar camera/export behavior for this release.

## 6. User Data Upload

- [ ] Confirm the bundled zero-value sample `local_data/user_data.xlsx` is
      labeled `User Excel data` and appended once to each reference source
      without entering browser-upload session state.
- [ ] Confirm the public sample contains no researcher measurements and that
      researcher-owned data are configured through an external path.
- [ ] Confirm the User Data Check & Quick Visualizer upload workflow works.
- [ ] Confirm uploaded data are visually distinguishable from reference data.
- [ ] Confirm uploaded data remain session-only and are not saved to disk or server storage.
- [ ] Confirm common column aliases are standardized where supported.
- [ ] Confirm uploaded-data quality summaries are visible where supported.
- [ ] Confirm the User Data Check & Quick Visualizer accepts CSV/XLSX uploads and keeps them session-only.

## 7. Local-Only And Development Pages

- [x] Exclude `pages/99_Environment_Check.py` from the public repository and deployment; retain it only in the local development working copy.
- [x] `pages/05_User_Data_Check_Quick_Visualizer.py` is the public User Data Check & Quick Visualizer for upload-first quality review and 2D/3D/4D exploration.
- [ ] Decide whether beta pages should be shown publicly, hidden, or documented as experimental.
- [ ] Confirm no private notes, restricted data, or unpublished datasets are included in public deployment files.

## 8. Tests

- [ ] Run the core test suite:

```bash
pytest -q test/test_envgeo_utils.py test/test_repository_health.py
```

- [ ] Run the broader test suite when preparing a GitHub release:

```bash
pytest
```

- [ ] Review any skipped or expected-failing tests.
- [ ] If a test fails because of an intentional page-list change, update the test or document the reason.

## 9. Documentation

- [x] Confirmed `README.md` reflects the current public-facing state.
- [x] Confirmed `README_Japanese.md` reflects the current public-facing state.
- [x] Confirmed `data_text/update_log.md` includes the latest unreleased changes.
- [x] Confirmed `data_text/update_log_Japanese.md` includes the latest unreleased changes.
- [x] Confirmed beta, archive, and local-development pages are clearly described.
- [x] Confirmed citation and data-source guidance are understandable.
- [x] Created the bilingual, figure-supported static documentation website from
  the reviewed manuals. It documents the stable public scope only and contains
  no private paths, data, tokens, or internal records.
- [x] Published the documentation website through GitHub Pages and verified the
  public URLs, navigation, images, and links:
  <https://envgeo.github.io/seawater_map/>.
- [ ] Update the laboratory website after the stable URL, release version,
  public-page scope, documentation URL, and Zenodo DOI are final. Keep its
  description aligned with the stable `seawater_map` release: approximately
  50,000 cited records including NASA GISS and PAGES CoralHydro2k, and the
  user-data upload/plot capability. Do not retain superseded version numbers,
  draft DOI wording, or pages excluded from the stable release.

## 10. GitHub Release Preparation

- [x] Confirmed the `seawater_map` repository and `main` branch as the stable-release destination.
- [ ] Confirm no temporary files, private files, downloaded reports, or local cache files are staged.
- [ ] Review changed files before committing.
- [x] Used a clear release-preparation commit message (`948b384`).
- [x] Tagged the reviewed stable commit as `v1.3.4` after the local and CI checks.

## 11. Streamlit Deployment

- [ ] Confirm the deployment repository includes required files:
  - `home.py`
  - `envgeo_utils.py`
  - `pages/`
  - `dataset/`
  - `data/`
  - `data_text/`
  - `coastline/`
  - `requirements.txt`
  - `runtime.txt` if used by the deployment platform.
- [ ] Confirm excluded local-only pages are actually excluded if needed.
- [ ] Open the deployed app and repeat a short smoke test:
  - Home opens.
  - T-S page opens.
  - Mapping page opens.
  - Depth Profile opens.
  - User Data Check & Quick Visualizer opens.

## 12. Package-index publication (PyPI)

- [x] Built the intended final distribution artifact and ran `twine check`.
- [x] Inspected the TestPyPI project page for README rendering. Before the PyPI
      upload, replace README links and image references that are relative to the
      repository with durable absolute GitHub or GitHub Pages URLs as needed.
      TestPyPI files are immutable; a broken relative link found there must be
      corrected in the final source before the separate PyPI upload.
- [x] Uploaded the intended artifact to TestPyPI and installed it in a new macOS
      environment. Use conda-forge only for compiled geospatial prerequisites
      where required, then install this package with `pip`.
- [x] Confirmed the TestPyPI installation can launch the application and repeated
      the short smoke test.
- [x] After the final tag was verified, published the same reviewed artifact to
      PyPI as `envgeo-seawater`, using Trusted Publishing or a secure manual
      upload; never commit a PyPI token.
- [x] Repeated the clean macOS `pip install envgeo-seawater` and launch check.
- [ ] A conda-forge recipe/feedstock is a useful later improvement, but is not
      a v1.3.4 blocker once the PyPI path is verified.

## 13. Zenodo / DOI Preparation

- [x] Enabled the `seawater_map` GitHub repository in Zenodo before creating the
      GitHub Release, so that the tagged release is automatically archived.
- [x] Confirmed the GitHub Release was final before creating the Zenodo archive.
- [ ] Confirm title, authors, affiliations, license, and description.
- [x] Confirmed the archived version matches release tag `v1.3.4`.
- [x] Recorded the wheel SHA-256 from a wheel rebuilt from the clean tagged
      checkout. CI wheel artifacts are inspection evidence, not release or
      Zenodo distribution files.
- [x] Recorded the version DOI (`10.5281/zenodo.23117784`) and concept DOI
      (`10.5281/zenodo.23117783`) in the README and citation files
      after the archive is created. This follow-up documentation commit is not
      part of the immutable tagged archive unless a DOI was reserved in advance.

## 14. JOSS-Oriented Follow-Up

- [ ] Prepare a separate `docs/joss_checklist.md` before resubmission.
- [ ] Confirm pytest coverage is meaningful and not only superficial.
- [ ] Confirm examples and user documentation are sufficient for reviewers.
- [ ] Confirm installation instructions are reproducible on a clean environment.
- [ ] Confirm citation instructions include both EnvGeo-Seawater and original data providers.
