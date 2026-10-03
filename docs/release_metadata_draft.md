# Release and Zenodo Metadata Draft

[日本語版](release_metadata_draft_Japanese.md)

This is the finalized metadata record for the v1.3.4 GitHub Release and Zenodo
archive. The immutable release archive is the tagged commit; this document is
the subsequent public documentation record.

## Core metadata

| Field | Draft value |
|---|---|
| Title | EnvGeo-Seawater: An Interactive Platform for Exploring Seawater Isotope and Hydrographic Data |
| Release label | EnvGeo-Seawater v1.3.4 |
| Version | 1.3.4 |
| Author | Toyoho Ishimura |
| ORCID | <https://orcid.org/0000-0001-9708-3743> |
| Affiliation | Graduate School of Human and Environmental Studies, Kyoto University, Japan |
| License | MIT |
| Source repository | <https://github.com/envgeo/seawater_map> |
| Release date | 2026-10-03 |
| Release commit | `948b384455480f06b7a9b6b0a7a3e53af7135e35` |
| Version DOI | <https://doi.org/10.5281/zenodo.23117784> |
| Concept DOI (all versions) | <https://doi.org/10.5281/zenodo.23117783> |
| Zenodo record | <https://zenodo.org/records/23117784> |

## Short description

EnvGeo-Seawater is an interactive Python and Streamlit platform for exploring
seawater isotope and hydrographic data. It integrates approximately 50,000
cited records, including NASA GISS and PAGES CoralHydro2k reference datasets,
with regional reference data and the Kodama et al. (2024) Japan-region core
collection. The application supports mapping, 2D–4D visualization,
salinity–isotope relationships, T–S diagrams, depth profiles, vertical
sections, and session-only comparison with user-supplied data.

## Keywords

`seawater isotopes`; `oceanography`; `hydrography`; `stable isotopes`; `data
visualization`; `Streamlit`; `Python`

## Stable-release scope

The stable public repository contains pages 03, 04, 05, 31, 32, 34, 35, 37,
53, and historical archive page 80. Development pages 90 and 91, and the
local diagnostic Page 99, are excluded from the stable release, its wheel,
GitHub Release, and Zenodo archive.

## Release completion record

1. The reviewed commit was tagged as `v1.3.4` and released on GitHub.
2. A clean tagged checkout produced a wheel with SHA-256
   `ae3cf31365758b639e08d41497ac15452a8738db07f422b973b969c5eb3258f7`.
3. The matching source distribution SHA-256 is
   `8b319ac4b3176c7280be402b858fa2e2da17e3deac476ce064b7cb9baf29e61c`.
4. PyPI and TestPyPI installations were verified on a clean macOS environment.
5. Zenodo archived the GitHub Release as record 23117784. The version DOI is
   used for citations; the concept DOI is used for the README badge.

The citation instruction remains: cite EnvGeo-Seawater **and** each original
data provider used in the analysis.
