import streamlit as st  
import time 

from src.ui.base_layout import style_background_dashbord, style_base_layout
from src.components.header_home import header_dashboard
from src.database.db import check_teacher_exists, create_teacher, teacher_login
from src.pipeline.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipeline.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student

import tkinter as tk
from PIL import Image, ImageTk   
import numpy as np

def student_dashboard():
    st.header("student dashboard header")

def student_screen():

    style_background_dashbord()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return 
    
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

    # # 1. Camera Input
    # camera_photo = st.camera_input("Position the face in the center of the screen")

    # # 2. File Uploader
    # uploaded_photo = st.file_uploader("Or upload a photo", type=["jpg", "jpeg", "png"])

    # # 3. Determine Source
    # photo_source = None

    # if camera_photo:
    #     photo_source = camera_photo
    # elif uploaded_photo:
    #     photo_source = uploaded_photo

    photo_source = st.camera_input("Position the face in the center of the screen")

    show_registration = False
    if photo_source:

        img = np.array(Image.open(photo_source))
       

        with st.spinner('AI is scanning.....'):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning('Face not found!')
            elif num_faces > 1:
                st.warning('Multiple faces found')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id'] == student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f"Welcome Back {student['name']}")
                        import time
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info('Face not recognized! you might be new student')
                    show_registration = True
        
    if show_registration:
        with st.container(border=True):
            st.header('Register new Profile')
            new_name = st.text_input("Enter your name", placeholder='E.g. Hamza Rizvi')

            st.subheader('Optional : Voice Enrollment')
            st.info("Enroll your for voice only attendance")


            audio_data = None

            try:
                audio_data = st.audio_input('Record a short phrase like I am present, My name is Akash.')
            except Exception:
                st.error('Audio Data failed!')

            if st.button('Create Account', type='primary'):
                if new_name:
                    with st.spinner('Creating profile..'):
                        img = np.array(Image.open(photo_source))
                        encodings= get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f'Profile Created! Hi {new_name}!')
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error('Couldnt capture your facial features for registration')

                else:
                    st.warning('Please enter your name!')

