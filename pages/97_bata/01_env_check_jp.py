import streamlit as st
import sys
import subprocess
import os

st.title("🛠 環境診断ツール")

st.header("1. 実行パスの確認")
st.write(f"**Pythonの場所:** `{sys.executable}`")
st.write(f"**Streamlitの場所:** `{st.__file__}`")

st.header("2-1. 主要ライブラリのチェック1")
libraries = ["streamlit", "plotly", "gsw", "pandas", "cartopy", "sklearn","scipy"]
results = {}

for lib in libraries:
    try:
        module = __import__(lib)
        results[lib] = {"status": "✅ OK", "version": getattr(module, "__version__", "unknown")}
    except ImportError:
        results[lib] = {"status": "❌ 未インストール", "version": "-"}

st.table(results)

st.header("2-2. 主要ライブラリのチェック2")
libraries = ["numpy","matplotlib","openpyxl",  "statsmodels", "streamlit-plotly-events"]
results = {}

for lib in libraries:
    try:
        module = __import__(lib)
        results[lib] = {"status": "✅ OK", "version": getattr(module, "__version__", "unknown")}
    except ImportError:
        results[lib] = {"status": "❌ 未インストール", "version": "-"}

st.table(results)


st.header("3. パスの整合性診断")
if "anaconda3/envs/envgeo_streamlit134" in sys.executable:
    st.success("OK！: 現在、Anacondaの仮想環境内で正しく動作しています。")
elif "homebrew" in sys.executable.lower():
    st.error("警告: まだ Homebrew 版の Python を使っています。これでは仮想環境のライブラリが見えません。")
else:
    st.warning("注意: 意図しない Python パスで動作している可能性があります。")

st.header("4. インストール済み全リスト")
if st.button("詳細リストを表示"):
    result = subprocess.run(["pip", "list"], capture_output=True, text=True)
    st.text(result.stdout)
