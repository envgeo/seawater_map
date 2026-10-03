# EnvGeo-Seawater Release Checklist

[English version](release_checklist.md)

テストサイトの更新、GitHub更新、Release作成、Zenodoへのversion archiveの前に、このchecklistを使います。

`seawater_map`は正式な安定版repositoryです。このchecklistは、tagを付けるGitHub Release、Zenodo archive、
JOSS向けsoftware recordに用います。

## 1. ローカル環境

### 安定版1.3.4（2026-10-03）

- [x] 最終試験にはPython 3.12／Streamlit 1.63／Plotly 5.24環境を使用した。
- [x] 安定版CI run #5（2026-10-03）はPython 3.10と3.12で成功した。test、wheel作成、
  隔離wheel導入、Python版ごとのwheel artifact保存を完了した。

### 既に行った手動smoke確認（release commit後に再確認する）

以下はRelease candidateの確認中に完了した探索的な手動確認である。有用な根拠ではあるが、commit済みの
安定版Releaseとdeploymentに対する最終手動確認の代わりにはしない。

- [x] Homeが開き、ローカル専用の`99_Environment_Check.py`が公開sidebarに表示されなかった。
- [x] Mapping、T–S Diagram、Depth Profileがアプリケーションerrorなしで開き、データ選択と
      `Apply settings`で表示結果が更新された。
- [x] Mappingの背景tileが表示された。
- [x] アプリケーションerror画面は出なかった。ローカル絶対pathとcredentialらしき値については、
      別途、公開fileとwheelの静的監査を行った。

- [ ] 意図したPython環境が有効であることを確認する。
- [ ] 検証済み基準の一つを使っていることを確認する：Python 3.10.15／Streamlit 1.42、または
  Python 3.12.14／Streamlit 1.63（どちらもPlotly 5.24）。
- [ ] `requirements.txt`が検証した環境と一致することを確認する。
- [ ] 必要に応じてローカル環境診断ツールを起動する。

```bash
streamlit run tools/env_check_streamlit.py
```

- [ ] Release記録に必要な場合、環境reportをCSVまたはPDFとして保存する。

## 2. 基本起動

- [ ] アプリをローカルで起動する。

```bash
streamlit run home.py
```

- [ ] `home.py`が正常に開くことを確認する。
- [ ] アプリに`1.3.4 (2026-09-28)`と表示されることを確認する。
- [ ] HomeのMain、About、Data Sources、Manual、Update History、日本語情報のtabが読み込まれることを確認する。

## 3. Sidebarとfilter

- [ ] sidebarに`Data filtering`が表示されることを確認する。
- [ ] `Apply settings`をクリックする案内が見えることを確認する。
- [ ] `Area filter preset`が初期Longitude／Latitude範囲を変更することを確認する。
- [ ] area preset選択後もLongitude／Latitude sliderを手動調整できることを確認する。
- [ ] filter変更後に`Apply settings`で図が更新されることを確認する。
- [ ] `Details and statistics of filtered data`が開き、CSVを正しく出力できることを確認する。

## 4. 主な可視化ページ

各ページを開き、簡単な視覚確認を行います。

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

各ページについて、次を確認します。

- [ ] data source選択が動く。
- [ ] `Apply settings`後にfilterが動く。
- [ ] 主な図がerrorなく描画される。
- [ ] caption、help button、labelが理解できる。
- [ ] 該当する場合、`Sampling Location Map`が正しく描画される。
- [ ] 該当する場合、`Map controls`と`Map style`が動く。
- [ ] 明らかな文字重なりやlayout崩れがない。

## 5. 図の出力

- [ ] 2D Matplotlib図の下に`Download image`が表示されることを確認する。
- [ ] ダウンロードしたPNGが正しく開くことを確認する。
- [ ] 特にDepth Profileで、図titleがダウンロード画像内に収まることを確認する。
- [ ] file nameが適切で危険な文字を含まないことを確認する。
- [ ] このReleaseで、Plotly図・地図をPlotly modebarのcamera／export機能に委ねるかを判断する。

## 6. ユーザーデータupload

- [ ] 同梱するゼロ値sample `local_data/user_data.xlsx`が`User Excel data`と表示され、
  browser uploadのsession stateに入らず各参照sourceへ1回だけ加わることを確認する。
- [ ] 公開sampleに研究者の測定値が含まれず、研究者自身のdataは外部pathで設定することを確認する。
- [ ] User Data Check & Quick Visualizerのupload workflowが動くことを確認する。
- [ ] upload dataが参照dataと視覚的に区別できることを確認する。
- [ ] upload dataがsession-onlyで、diskまたはserver storageに保存されないことを確認する。
- [ ] 対応する場合、一般的な列aliasが標準化されることを確認する。
- [ ] 対応する場合、upload dataのquality summaryが見えることを確認する。
- [ ] User Data Check & Quick VisualizerがCSV/XLSX uploadを受け付け、session-onlyで扱うことを確認する。

## 7. ローカル専用・開発用ページ

- [x] `pages/99_Environment_Check.py`を公開repositoryとdeploymentから除外し、ローカル開発作業copyだけに残す。
- [x] `pages/05_User_Data_Check_Quick_Visualizer.py`は、upload-firstのquality確認と2D/3D/4D探索のための公開User Data Check & Quick Visualizerである。
- [ ] beta pageを公開表示するか、隠すか、実験的と明記するかを判断する。
- [ ] private note、制限data、未公表datasetが公開deployment fileに含まれないことを確認する。

## 8. テスト

- [ ] core test suiteを実行する。

```bash
pytest -q test/test_envgeo_utils.py test/test_repository_health.py
```

- [ ] GitHub Release準備時は、より広いtest suiteを実行する。

```bash
pytest
```

- [ ] skipまたはexpected failureのtestを確認する。
- [ ] 意図したpage list変更でtestが失敗した場合は、testを更新するか理由を記録する。

## 9. 文書

- [x] `README.md`が現在の公開状態を反映することを確認した。
- [x] `README_Japanese.md`が現在の公開状態を反映することを確認した。
- [x] `data_text/update_log.md`に最新の未release変更があることを確認した。
- [x] `data_text/update_log_Japanese.md`に最新の未release変更があることを確認した。
- [x] beta、archive、local-development pageが明確に説明されることを確認した。
- [x] 引用・data sourceの案内が理解できることを確認した。
- [x] 精査済みmanualを基に、図付きの英日静的ドキュメントwebsiteを作成した。安定版の公開範囲だけを説明し、private path、個人データ、token、内部記録を含めないことを確認した。
- [x] GitHub Pagesでドキュメントwebsiteを公開し、公開URL、navigation、図、linkを確認した：<https://envgeo.github.io/seawater_map/>。
- [ ] 安定版URL、release version、公開ページ範囲、ドキュメントURL、Zenodo DOIが確定した後に、研究室websiteを更新する。安定版`seawater_map`の説明と一致させ、NASA GISSとPAGES CoralHydro2kを含む引用付き約50,000件のデータ、ユーザーデータのアップロード／プロット機能を記載する。旧いversion番号、DOIの保留表現、安定版から除外したページの説明を残さない。

## 10. GitHub Release準備

- [x] 安定版Releaseの対象を`seawater_map` repositoryの`main` branchとして確認した。
- [ ] temporary file、private file、downloadしたreport、local cache fileがstageされていないことを確認する。
- [ ] commit前に変更ファイルを確認する。
- [x] Release準備範囲を説明する明確なcommit message（`948b384`）を使用した。
- [x] ローカル確認とCIの確認後に、review済みstable commitへ`v1.3.4` tagを付けた。

## 11. Streamlit deployment

- [ ] deployment repositoryに必要なfileが含まれることを確認する。
  - `home.py`
  - `envgeo_utils.py`
  - `pages/`
  - `dataset/`
  - `data/`
  - `data_text/`
  - `coastline/`
  - `requirements.txt`
  - deployment platformが使う場合は`runtime.txt`
- [ ] 必要な場合、除外対象のlocal-only pageが実際に除外されていることを確認する。
- [ ] deployment appを開き、短いsmoke testを繰り返す。
  - Homeが開く。
  - T-S pageが開く。
  - Mapping pageが開く。
  - Depth Profileが開く。
  - User Data Check & Quick Visualizerが開く。

## 12. Package indexでの公開（PyPI）

- [x] 想定した最終distribution artifactをbuildし、`twine check`を実行した。
- [x] TestPyPI project pageでREADMEの表示を確認した。PyPI upload前に、repository内では
      有効でもpackage index上では切れる相対link・画像参照を、必要に応じて永続的な
      GitHubまたはGitHub Pagesの絶対URLへ置換する。TestPyPIの配布fileはimmutableなので、
      そこで見つかった相対linkの不備は、別サービスであるPyPI upload前に最終sourceで修正する。
- [x] 想定artifactをTestPyPIへuploadし、新しいmacOS environmentでinstallした。
      必要なcompiled geospatial prerequisiteだけをconda-forgeから入れ、その後に
      `pip`で本packageをinstallする。
- [x] TestPyPI installationからappを起動し、短いsmoke testを繰り返した。
- [x] 最終tagの確認後、同じreview済みartifactをPyPIの`envgeo-seawater`として公開した。
      Trusted Publishingまたは安全な手動uploadを使用し、PyPI tokenをcommitしない。
- [x] 新しいmacOS environmentで`pip install envgeo-seawater`と起動確認を再現した。
- [ ] conda-forge recipe/feedstockは有用な後続改善とする。ただしPyPI経路を確認できれば、
      v1.3.4とJOSS再投稿のblockerとはしない。

## 13. Zenodo／DOI準備

- [x] GitHub Release作成前に、`seawater_map` GitHub repositoryをZenodoで有効化し、
      tag付きReleaseが自動archiveされるようにする。
- [x] Zenodo archiveを作る前にGitHub Releaseが最終版であることを確認した。
- [ ] title、author、affiliation、license、descriptionを確認する。
- [x] archiveしたversionがRelease tag `v1.3.4`と一致することを確認した。
- [x] wheel SHA-256は、clean tagged checkoutから再作成したwheelの値だけを記録した。
      CI wheel artifactは確認根拠であり、ReleaseまたはZenodoの配布fileではない。
- [x] archive作成後に、version DOI（`10.5281/zenodo.23117784`）とconcept DOI
      （`10.5281/zenodo.23117783`）をREADMEとcitation filesへ記録した。
      DOIを事前予約しない限り、このfollow-up document commitはimmutableなtag付きarchiveには含まれない。

## 14. JOSS向けの後続作業

- [ ] 再投稿前に別途`docs/joss_checklist.md`を作成する。
- [ ] pytest coverageが表面的なものだけでなく意味を持つことを確認する。
- [ ] reviewerに十分なexampleとユーザー文書があることを確認する。
- [ ] clean environmentでinstallation手順を再現できることを確認する。
- [ ] citation instructionsにEnvGeo-Seawaterと元data providerの両方を含める。
