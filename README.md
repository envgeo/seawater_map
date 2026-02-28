# Under construction / 作成中です

# Seawater Japan: Interactive 3D-4D Seawater Isotope & Geochemical Database

[English](#english-section) | [日本語](#japanese-section)

---

<a name="english-section"></a>

## English

### Overview
**Seawater Japan** is a high-performance, web-based analytical platform designed for the visualization and exploration of seawater isotope geochemistry. Focusing on the marginal seas around Japan and global oceans, this tool integrates high-resolution datasets of stable isotopes ($\delta^{18}$O and $\delta$D), salinity, and temperature into an interactive 3D/4D environment.

### Key Features
* **Multi-Dimensional Visualization**: Explore spatial and temporal variations using 3D scatter plots and 4D time-series animations.
* **Advanced Geochemical Analysis**: Real-time generation of T-S diagrams, Salinity-$\delta^{18}$O regression lines, and vertical depth profiles.
* **Comprehensive Database**: Integrated data from Kodama et al. (2024), NASA GISS, and multiple historical maritime surveys.
* **User Data Integration**: A dedicated uploader allows researchers to visualize their own Excel datasets within the platform's analytical framework.
* **Cross-Platform Performance**: Built with Streamlit and Plotly for seamless operation directly in the web browser.

### Project Structure
* `home.py`: The main entry point of the application.
* `envgeo_utils.py`: Core utility module for data caching, filtering, and configuration.
* `pages/`: Contains specialized analytical modules (3D/4D visualizers, mapping, etc.).
* `data/`: Directory for database files and sample datasets.

### How to Use
1. **Access**: Visit the Web App at: [https://envgeo-seawater-map.streamlit.app](https://envgeo-seawater-map.streamlit.app)
2. **Navigation**: Use the sidebar to switch between specialized modules (3D Visualizer, Mapping, T-S Diagram, etc.).
3. **Data Selection**: Choose data sources (Japan Sea / Around Japan / Global) and filter by specific transects or cruises.
4. **Export**: Download generated figures and filtered datasets directly from the interface.

### Citation
If you use this tool or its integrated datasets for your research, please cite the following:
* **Software**: Ishimura, T. (2026). Seawater Japan: Interactive 3D-4D Seawater Isotope & Geochemical Database. DOI: [Insert DOI here]
* **Primary Data Source**: Kodama, T., et al. (2024). Spatiotemporal variations of seawater $\delta^{18}$O and $\delta$D in the Western North Pacific. *Geochemical Journal*.

---

<a name="japanese-section"></a>

## 日本語

### 概要
**Seawater Japan** は、海水の同位体地球化学データの可視化と解析に特化した高性能なWebベースプラットフォームです。日本周辺海域および世界海洋の安定同位体比（$\delta^{18}$O, $\delta$D）、塩分、水温のデータを統合し、インタラクティブな3D/4D環境で探索することを可能にします。

### 主な機能
* **多次元可視化**: 3D散布図および4D時系列アニメーションを用いた、時空間的なバリエーションの把握。
* **高度な地球化学解析**: T-S図、塩分-$\delta^{18}$O回帰直線、鉛直プロファイルなどのリアルタイム生成。
* **統合データベース**: Kodama et al. (2024)、NASA GISS、および複数の既往研究のデータを一括管理。
* **ユーザーデータ統合**: アップローダー機能により、研究者自身が持つExcelデータを本プラットフォームの解析機能で可視化可能。
* **ブラウザ完結型**: StreamlitとPlotlyを採用し、インストール不要で高速に動作します。

### プロジェクト構成
* `home.py`: アプリケーションのメインエントリポイント。
* `envgeo_utils.py`: データキャッシュ、フィルタリング、設定を管理するコアモジュール。
* `pages/`: 3D/4Dビジュアライザー、マッピング等の専門解析モジュール群。
* `data/`: データベースファイルおよびサンプルデータ。

### 使用方法
1. **アクセス**: Webアプリ URL: [https://envgeo-seawater-map.streamlit.app](https://envgeo-seawater-map.streamlit.app)
2. **ナビゲーション**: サイドバーから各機能（3D Visualizer, Mapping, T-S Diagram 等）を選択します。
3. **データ選択**: データソース（日本海 / 日本周辺 / 全球）を選択し、特定の海域や観測航海でフィルタリングします。
4. **出力**: 生成された図表やフィルタリング後のデータセットを直接ダウンロードできます。

### 引用について
本ツールおよび統合データを使用される場合は、以下の引用をお願いいたします。
* **ソフトウェア**: 石村豊穂 (2026). Seawater Japan: Interactive 3D-4D Seawater Isotope & Geochemical Database. DOI: [ここにDOIを記載]
* **主要データソース**: Kodama, T., et al. (2024). Spatiotemporal variations of seawater $\delta^{18}$O and $\delta$D in the Western North Pacific. *Geochemical Journal*.

Developed by **Toyoho Ishimura** (Associate Professor, Kyoto University)
