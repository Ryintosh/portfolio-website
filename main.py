import streamlit as st
import requests
from streamlit_lottie import st_lottie
from st_click_detector import click_detector
import webbrowser


        
st.set_page_config(page_title="Ryan's Portfolio", page_icon=":tada", layout = 'wide')

left_column, right_column = st.columns((3,1))

with left_column:
    st.title("Hello, I am Ryan McIntosh")
    st.subheader("Site Reliability Engineer")
    st.write("I am passionate about cloud automation, incident management, and monitoring to improve systems reliability")

with right_column:
    st.image("hitachipic.png", width = 125)

st.write("----")

st.subheader("Work Experience")

left_columnhv, right_columnhv = st.columns((3,1))

with left_columnhv:
    st.write(
    """

    Site Reliability Engineer for Hitachi Vantara:
    - Collaborated with a Multinational Pharmaceutical Industry to provide incident management, deployments, and cloud automation. 
    - Developed a dashboard as code script, which created new dashboards for new resources introduced into production and updated all pre-existing dashboards. 
    - Monitored production utilizing Azure Data Explorer, Azure App Insights, and Azure EventHub Namespaces. 
    - Created standard operating procedures for groups to update pre-existing dashboards with a JSON file using Azure CLI, as there is no current functionality to do this using Azure Portal.

    """)

with right_columnhv:
    st.image("hitachivantarasymbol.jpg", width=200)

left_columnrev, right_columnrev = st.columns((3,1))

with left_columnrev:
    st.write(
    """
    Site Reliability Engineer Contractor for Revature:
    - Produced multiple projects utilizing Agile for group management. 
    - Applied Kubernetes, Jenkins, Grafana, Java, PostgreSQL, Prometheus, Terraform, and Loki in technical applications to these projects. 
    - From banking applications in Java to digitizing a web application to an EKS, Provided monitoring of those applications and the creation of Service Level Objectives. 
    - The monitoring dashboards and alerts created for these applications were mainly produced with my efforts, the main focus being that the information should be meaningful, simple, and foretelling.
    """)

with right_columnrev:
    st.image("revaturepic.png", width = 200)

content = """
<a href='#' id='github'><img width='4%' src="https://th.bing.com/th/id/OIP.D_Gm8IGCvkqmOgtU2hueVwHaHS?pid=ImgDet&rs=1" hspace="50" class = "center"></a>
<a href='#' id='linkedin'><img width='4%' src='https://yt3.ggpht.com/-CepHHHB3l1Y/AAAAAAAAAAI/AAAAAAAAAAA/Z8MftqWbEqA/s900-c-k-no/photo.jpg' hspace="50" class = "center"></a>
<a href='#' id='youtube'><img width='4%' src='https://th.bing.com/th/id/OIP.BzZJPmzidrI77XpMNfnBFwHaHa?pid=ImgDet&rs=1' hspace="50" class = "center"></a>
    """


click = click_detector(content)
if click == "github":
    webbrowser.open_new_tab("https://github.com/Ryintosh")
elif click == "linkedin":
    webbrowser.open_new_tab("https://www.linkedin.com/in/ryanmac12356/")
elif click == "youtube":
    webbrowser.open_new_tab("google.com")


