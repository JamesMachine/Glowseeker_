import streamlit as st

st.set_page_config(
    page_title="Glowseeker", page_icon="🖼️", initial_sidebar_state="collapsed"
)

st.markdown("<h1 style='text-align: center; color: grey;'>Skin Scan</h1>", unsafe_allow_html=True)

st.image("skin_scan.png")

st.write("")
st.camera_input("cam_in")