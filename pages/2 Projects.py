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


tabName = deepcopy(repoName)
repoName.remove("Ryintosh")


def getReadMe(repo,owner,branch):
    test = requests.get(url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/README.md")
    return test


repoName = st.tabs(repoName)

i=0
while i <= len(repoName) - 1:
    if tabName[i] != "Ryintosh":
        with repoName[i]:
            response = getReadMe(tabName[i],owner,branch)
            st.write(response.text)
        i = i + 1
