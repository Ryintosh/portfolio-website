import streamlit as st
import requests
from streamlit_lottie import st_lottie
from st_click_detector import click_detector
import webbrowser
from github import Github


username = "Ryintosh"

g = Github()
# get that user by username
user = g.get_user(username)

for repo in user.get_repos():
    st.write(repo)