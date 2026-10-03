# Release・Zenodoメタデータ下書き

[English version](release_metadata_draft.md)

これはv1.3.4のGitHub ReleaseとZenodo archiveについて確定したメタデータ記録である。immutableな
release archiveはtag付きcommitであり、この文書はその後に加えた公開文書の記録である。

## 基本メタデータ

| 項目 | 下書き値 |
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
| Concept DOI（全version） | <https://doi.org/10.5281/zenodo.23117783> |
| Zenodo record | <https://zenodo.org/records/23117784> |

## 短い説明文

EnvGeo-Seawaterは、海水安定同位体と水文データを探索するためのPython／Streamlitによる
インタラクティブなplatformである。NASA GISSおよびPAGES CoralHydro2kの比較用dataset、地域参照data、
Kodama et al. (2024)の日本周辺core collectionを含む、約50,000件の引用付きrecordを統合する。地図、
2D–4D可視化、塩分–同位体関係、T–S diagram、深度profile、鉛直section、利用者dataとのsession限定比較を
提供する。

## Keywords

`seawater isotopes`；`oceanography`；`hydrography`；`stable isotopes`；`data visualization`；
`Streamlit`；`Python`

## 安定版の公開範囲

安定版public repositoryにはPage 03、04、05、31、32、34、35、37、53、および履歴archiveのPage 80を含める。
開発用Page 90・91とローカル診断Page 99は、安定版Release、wheel、GitHub Release、Zenodo archiveから除外する。

## Release完了記録

1. review済みcommitに`v1.3.4` tagを付け、GitHub Releaseを公開した。
2. clean tagged checkoutから作成したwheelのSHA-256は
   `ae3cf31365758b639e08d41497ac15452a8738db07f422b973b969c5eb3258f7`である。
3. source distributionのSHA-256は
   `8b319ac4b3176c7280be402b858fa2e2da17e3deac476ce064b7cb9baf29e61c`である。
4. PyPIとTestPyPIからの導入をclean macOS環境で検証した。
5. ZenodoはGitHub Releaseをrecord 23117784としてarchiveした。引用にはversion DOI、README
   badgeにはconcept DOIを使用する。

引用時には、EnvGeo-Seawater **および** 解析で使った各元データ提供者を引用する。
