import streamlit as st
import pandas as pd
from sklearn import datasets


@st.cache_resource
def load_data():
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target_names[iris.target]
    return df


df = load_data()
targets = list(df.target.unique())
selected_targets = st.multiselect('select targets', targets, default=targets)
df = df[df.target.isin(selected_targets)]

st.dataframe(df.style.highlight_max(axis=0))

df.hist()
st.pyplot()