# EnvGeo-Seawater 文書一覧

このディレクトリには、トップレベルREADMEより詳しいプロジェクト文書を収録します。
有用な履歴・開発記録も残しますが、Releaseの承認や安定版の公開範囲を示すものではありません。

[English version](README.md)

## 現在の文書

- `release_checklist.md` / `release_checklist_Japanese.md`
  ローカル試験、Streamlit deployment、GitHub Release準備、Zenodo／DOI archiveの確認項目。

- `stable_release_publication_notes.md` / `stable_release_publication_notes_Japanese.md`
  安定版の公開範囲、除外対象、データとprivate fileの扱い、GitHub Release／Zenodoの順序を
  短くまとめた注意事項。

- `code_guide.md` / `code_guide_Japanese.md`
  中心モジュール、安定版ページ、資産ディレクトリ、コード文書化の目安を短く示す案内。

- `publication_content_review_checklist.md` /
  `publication_content_review_checklist_Japanese.md`
  安定版repositoryのコード、文書、データ、資産、除外対象をファイル単位で確認する
  公開前コンテンツチェックリスト。

- `sprint3_distribution_design_and_acceptance.md` /
  `sprint3_distribution_design_and_acceptance_Japanese.md`
  1.3.4安定版repositoryの現行配布設計・検証記録。「Sprint 3」の意味は文書内で説明する。

- `testing.md` / `testing_Japanese.md`
  現在のpytest suite、その範囲、限界、今後の拡充方針の公開向け説明。

- `streamlit_migration.md` / `streamlit_migration_Japanese.md`
  Python 3.12、Streamlit 1.63、Plotly互換性、環境比較、視覚確認に関する移行記録。

- `integrated_visualizer_strategy.md` / `integrated_visualizer_strategy_Japanese.md`
  個別ページ、共通ユーザーデータupload、Integrated Visualizerに関する開発時の構成・移行履歴。
  Page 90のワークフローは安定版の公開範囲には含めない。

- `development_notes.md` / `development_notes_Japanese.md`
  オフライン地図設計、ユーザーデータ構成、地理空間asset、保留作業、安全な整理条件に関する
  1.3.3時点の技術的な履歴。現在のRelease checklistではありません。

- `distribution_foundation_audit_and_plan.md` /
  `distribution_foundation_audit_and_plan_Japanese.md`、および
  `wheel_proof_report.md` / `wheel_proof_report_Japanese.md`
  Sprint 2における配布基盤監査とローカルwheel実証の履歴記録。後の配布設計に至った経緯を示すものであり、現行1.3.4の検証記録は`sprint3_distribution_design_and_acceptance*.md`です。

- `offline_operation_log.md` / `offline_operation_log_Japanese.md`
  オフライン／通信不安定時の地図動作、自己完結HTML出力、既知の制約、検証範囲。

- `manual/` / `manual_Japanese/`
  安定版の公開ワークフローを対象とした、ページ別の英日ユーザーマニュアル。今後作成する静的
  ドキュメントサイトの内容正本であり、研究室Webサイトの案内にも再利用できます。

## 今後作成する文書

- `joss_checklist.md`
  将来のJOSS再投稿に向けた、テスト、文書、例、引用、ライセンス、archive DOIの確認項目。
