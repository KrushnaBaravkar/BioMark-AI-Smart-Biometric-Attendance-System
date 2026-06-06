import streamlit as st  

from src.ui.base_layout import style_background_dashbord, style_base_layout
from src.components.header_home import header_dashboard
from src.database.db import check_teacher_exists, create_teacher, teacher_login

import PIL as Image
import numpy as np

def student_screen():

    style_background_dashbord()
    style_base_layout()

    col1, col2 = st.columns(2, vertical_alignment="center", gap="large")

    with col1:
        header_dashboard()

    with col2:
        if st.button("Go back to Home", type="secondary", key="loginbackbtn", shortcut="control + backspace"):
            st.session_state['login_type'] = None
            st.rerun
    # st.header("Register your teacher profile")
    st.markdown(
        """
        <h2 style='text-align:center; color:#1A1A1A'>
            Login your FaceID
        </h2>
        """,
        unsafe_allow_html=True
    )
    
    # adding space between header and the input boxes
    st.space()
    st.space()

    photo_source = st.camera_input("Position the face in the center of the screen")

    if photo_source:
        np.array(Image.open(photo_source))

        