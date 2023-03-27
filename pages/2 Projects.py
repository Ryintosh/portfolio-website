import streamlit as st
import requests
from github import Github
from copy import deepcopy


owner = "Ryintosh"
branch = "main"
repoName = []

g = Github()
user = g.get_user(owner)

for repo in user.get_repos():
    repoName.append(repo.name)


repoName.append("test")
temp = deepcopy(repoName)


def getReadMe(repo,owner,branch):
    test = requests.get(url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/README.md")
    return test


repoName = st.tabs(repoName)

i=0
while i <= len(repoName) - 1:
    with repoName[i]:
        response = getReadMe(temp[i],owner,branch)
        st.write(temp[i])
        st.write(response.text)
    i = i + 1