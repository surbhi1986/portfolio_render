import streamlit as st
import requests
# import streamlit_lottie as st_lottie
# from streamlit_lottie import st_lottie_spinner
import json
import time
from PIL import Image

st.set_page_config(page_title="My Webpaje", page_icon= ':tada:', layout="wide")

# def load_lottieurl(url):
#     r=requests.get(url)
#     if r.status_code!=200:
#         return None
#     return r.json()

# ---use local CSS ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ----- Header section --------
with st.container():
    st.subheader("Hi Everyone, I am Dr. Sharma :wave:")
    st.title("I am head of Data science department in an IT firm from India")
    st.write("I am passonate about computer vission and AI using python. I am a learer by heart")

# ----- load Assests 
# load_lotties=load_lottieurl(lottie_url = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
image = Image.open('media/Applications-of-Artificial-Intelligence.png')


# -----My Responsibilities
with st.container():
    st.write("---")
    left_column,  right_column=st.columns(2)
    with left_column:
        st.header("What are my responsibities:")
        st.write("##")
        st.write(
            """
            1. Lead and manage the data science team.
            2. Define and execute the data science strategy.,
            3. Collaborate with cross-functional teams to drive data-driven decisions.,
            4. Develop machine learning models for various business applications.,
            5. Analyze large datasets to extract actionable insights.,
            6. Mentor and coach data scientists on best practices.,
            7. Stay up-to-date with the latest advancements in data science and AI.,
            8. Ensure data privacy and security compliance.,
            9. Communicate findings and insights effectively to stakeholders.,
            10. Drive innovation and experimentation in data science projects.,
            """
        )
# # Streamlit app
    with right_column:
        st.image(image, caption='Application Areas of AI')
#         st.write(load_lotties, height=300, key="coding")
#         with st_lottie_spinner(load_lotties):
#             time.sleep(5)
#             st.balloons()
# ----Projects ---
with st.container():
    st.write("---")
    st.header("My Project")
    st.write('##')
    image_column, text_column=st.columns((1,2))
    with text_column:
        st.subheader("AI in Sports")
        st.write("""AI-Based Sports Coaching System: AI-based engine which analyze the body keyjoints  & recognizes player's 
body moments & gives suggestions to improve player's performance.

Tech Stacks: Python, Pytorch, MMCV, Time Series Analysis, Kubeflow, GCP, Flutter, Firebase
We addressed various challenges, including building an AI model for cricket utilizing image processing and computer vision. 
Our solution involved deploying a PyTorch-based engine on the cloud to extract 133 body key joints, analyze player recordings,
and provide feedback on improvement areas. Our system can also isolate the subject player from the team. Additionally,
we leveraged PyTorch, OpenCV, and GCP to build custom solutions and a machine learning pipeline. Our work encompassed 
object detection (person & ball), object tracking, pose estimation, SVM, LSTM, and a user-friendly mobile/web app for video uploads 
and AI-based feedback.
""")
    st.markdown("For more details")


# -----Contact------
with st.container():
    st.write("---")
    st.header("Get In touch with Me !")
    st.write("##")

    contact_form="""
    <form action="https://formsubmit.co/s.surbhi1986@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Write your message here" required></textarea> 
     <button type="submit">Send</button>
</form>
"""

left_column, right_column=st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()