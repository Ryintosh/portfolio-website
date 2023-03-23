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
    st.write("----")
    st.write("I have ")

with right_column:
    st.image("testnobackground.png", width = 300)

st.write("----")



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


