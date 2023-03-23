import streamlit as st
import requests
from streamlit_lottie import st_lottie
from st_click_detector import click_detector
import webbrowser


st.title("Work Experience")

left_columnhv, right_columnhv = st.columns((3,1))

with left_columnhv:
    st.subheader("Site Reliability Engineer for Hitachi Vantara")
    st.write(
    """

    
    - Collaborated with a Multinational Pharmaceutical Industry to provide incident management, deployments, and cloud automation. 
    - Developed a dashboard as code script, which created new dashboards for new resources introduced into production and updated all pre-existing dashboards. 
    - Monitored production utilizing Azure Data Explorer, Azure App Insights, and Azure EventHub Namespaces. 
    - Created standard operating procedures for groups to update pre-existing dashboards with a JSON file using Azure CLI, as there is no current functionality to do this using Azure Portal.

    """)

with right_columnhv:
    st.image("hitachivantarasymbol.jpg", width=200)

left_columnrev, right_columnrev = st.columns((3,1))

with left_columnrev:
    st.subheader("Site Reliability Engineer Contractor for Revature")
    st.write(
    """
    
    - Produced multiple projects utilizing Agile for group management. 
    - Applied Kubernetes, Jenkins, Grafana, Java, PostgreSQL, Prometheus, Terraform, and Loki in technical applications to these projects. 
    - From banking applications in Java to digitizing a web application to an EKS, Provided monitoring of those applications and the creation of Service Level Objectives. 
    - The monitoring dashboards and alerts created for these applications were mainly produced with my efforts, the main focus being that the information should be meaningful, simple, and foretelling.
    """)

with right_columnrev:
    st.image("revaturepic.png", width = 200)