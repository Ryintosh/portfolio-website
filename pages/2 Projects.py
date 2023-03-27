import streamlit as st



owner = "Ryintosh"
branch = "main"
repoName = ["portfolio-website", "temp", "temp"]


portfoliowebsite, tab2, tab3 = st.tabs(tabs = repoName)

with portfoliowebsite:
    with open("ReadMes/portfolio-website.md") as f:
        s = f.read()
    st.markdown(s)


