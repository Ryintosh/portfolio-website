import streamlit as st



        
st.set_page_config(page_title="Ryan's Portfolio", page_icon=":tada", layout = 'wide')

left_column, right_column = st.columns((4,5))

with left_column:
    st.title("Hello, I am Ryan McIntosh")
    st.subheader("Site Reliability Engineer")
    st.write("""
    
                I am passionate about cloud automation, incident management, and monitoring to improve systems reliability.
                Cloud automation for me isn't just a task to implement into our production environment, but rather a goal
                to eliminate human error and produce results at a higher rate while maintaining accuracy. I have utilized cloud
                automation in monitoring, as I found in this area that this was of the utmost importance. Monitoring effectively
                with the right tools allows for quick response times and an accurate understanding of what is happening in an
                incident. Also having dashboards and alerts automatically created for new resources introduced into an environment helps significantly
                decrease the manual work and time consumed by employees, but it also allows the business to make better cost analyses on their resources
                by seeing their utilization. My goal is to provide a business visibility into their systems, as one can only fix if they
                know what to fix.

    
    
    """)


with right_column:
    st.image("pictures/hitachipic.png")

st.write("----")

st.title("Work Experience")

left_columnhv, right_columnhv = st.columns((3,1))

with left_columnhv:
    st.subheader("Site Reliability Engineer for Hitachi Vantara")
    st.write(
    """

    
    - Collaborated with a Multinational Pharmaceutical Industry to provide incident management, deployments, cloud automation, and change management. 
    - Developed a dashboard as code script, which created new dashboards for new resources introduced into production and updated all pre-existing dashboards. 
    - Monitored production utilizing Azure Data Explorer, Azure App Insights, and Azure EventHub Namespaces. 
    - Created standard operating procedures for groups to update pre-existing dashboards with a JSON file using Azure CLI, as there is no current functionality to do this using Azure Portal.
    - Constructed Change Requests and presented in Change Advisory Boards the business impact of said changes.
    - Lead the development of alerts and dashboards for production.
    - Worked with a team to develop an Auth service utilizing Keycloak and Springboot
    - Architectured an Azure environment for a website contributing to the creation of a CI/CD pipeline making the Springboot application into an image hosted on an Azure Container Registry

    """)

with right_columnhv:
    st.image("pictures/hitachivantarasymbol.jpg", width=200)

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
    st.image("pictures/revaturepic.png", width = 200)


st.write("----")

st.title("Skills and Technologies")

tab1, tab2, tab3, tab4 = st.tabs(["Technical Skills", "Non-Technical Skills","Languages", "Technologies"])

with tab1:
    right, left = st.columns((1,1))
    with right:
        st.write("""
        - Cloud Automation
        - Monitoring
        - Incident Management
        - Scripting
        - CI/CD development
        - Version Control
        - Infrastructure Orchestration
        - Change Management
        """)

    with left:
        st.image("pictures/technicalskillspic.webp", width = 500)

with tab2:
    right, left = st.columns((1,1))
    with right:
        st.write("""
        - Communication
        - Problem-solving
        - Record-keeping
        - Leadership
        - Adaptability
        - Teamwork
        - Program Management
        """)

    with left:
        st.image("pictures/non-technicalskills.jpg", width = 500)
with tab3:
    right, left = st.columns((1,1))
    with right:
        st.write("""
        - Python
        - Java
        - Kusto
        - SQL
        - Terraform
        - Microsoft Azure CLI
        - Amazon Web Services CLI
        - Kubectl
        - Bash
        """)

    with left:
        st.image("pictures/languages.jpg", width = 500)

with tab4:
    right, left = st.columns((1,1))
    with right:
        st.write("""
        - Terraform
        - Jenkins
        - Azure Devops
        - Github
        - Github Actions
        - Chef Infra
        - Prometheus
        - Grafana
        - Microsoft Azure
        - Amazon Web Services
        - Kubernetes
        - Loki
        - Docker
        """)

    with left:
        st.image("pictures/technologies.jpg", width = 600)

st.write("----")






githubcolumn, linkedincolumn, youtubecolumn = st.columns(3)

with githubcolumn:
    content = """
<a href="https://github.com/Ryintosh" id='github'><img width="64" height="64" src="https://icons-for-free.com/iconfiles/png/512/code+collaboration+github+network+round+social+icon-1320086084536018107.png" alt = "GitHub" hspace="100" class = "center"></a>
    """
    st.write(content, unsafe_allow_html = True)
with linkedincolumn:
    content = """
<a href='https://www.linkedin.com/in/ryanmac12356/' id='linkedin'><img width='64' height='64' src="https://cdn.freebiesupply.com/logos/large/2x/linkedin-icon-logo-png-transparent.png" alt='LinkedIn' hspace="100" class = "center"></a>
    """
    st.write(content, unsafe_allow_html = True)


