import streamlit as st
import sys
import subprocess
import os

st.title("🛠 Environment Diagnostic Tool")

# --- 1. Execution Path Check ---
st.header("1. Execution Path Verification")
st.write(f"**Python Executable Path:** `{sys.executable}`")
st.write(f"**Streamlit Module Path:** `{st.__file__}`")

# --- 2. Library Dependency Checks ---
st.header("2-1. Core Library Check (Group 1)")
libraries_1 = ["streamlit", "plotly", "gsw", "pandas", "cartopy", "sklearn", "scipy"]
results_1 = {}

for lib in libraries_1:
    try:
        module = __import__(lib)
        results_1[lib] = {"status": "✅ OK", "version": getattr(module, "__version__", "unknown")}
    except ImportError:
        results_1[lib] = {"status": "❌ Not Installed", "version": "-"}

st.table(results_1)

st.header("2-2. Core Library Check (Group 2)")
libraries_2 = ["numpy", "matplotlib", "openpyxl", "statsmodels", "streamlit-plotly-events"]
results_2 = {}

for lib in libraries_2:
    try:
        module = __import__(lib)
        results_2[lib] = {"status": "✅ OK", "version": getattr(module, "__version__", "unknown")}
    except ImportError:
        results_2[lib] = {"status": "❌ Not Installed", "version": "-"}

st.table(results_2)

# --- 3. Path Integrity Diagnostics ---
st.header("3. Path Integrity Diagnosis")

# Check if running within the designated Anaconda environment
if "anaconda3/envs/envgeo_streamlit134" in sys.executable:
    st.success("Verified: Running correctly within the Anaconda virtual environment (envgeo_streamlit134).")
elif "homebrew" in sys.executable.lower():
    st.error("Warning: Homebrew-managed Python detected. This may prevent access to libraries in your virtual environment.")
else:
    st.warning("Notice: The Python path does not match the expected virtual environment. Please verify your execution context.")

# --- 4. Full Package List ---
st.header("4. Installed Packages Inventory")
if st.button("Display Detailed List (pip list)"):
    try:
        result = subprocess.run(["pip", "list"], capture_output=True, text=True)
        st.text(result.stdout)
    except Exception as e:
        st.error(f"Failed to retrieve package list: {e}")
