# pip install streamlit 
# pip install streamlit-image-select

import streamlit as st
import json

st.set_page_config(
    page_title="Glowseeker", page_icon="🖼️", initial_sidebar_state="collapsed"
)

st.sidebar.success("")

st.markdown("<h1 style='text-align: center; color: grey;'>Glowseeker_</h1>", unsafe_allow_html=True)

# left_co, cent_co,last_co = st.columns(3)
# with cent_co:
st.image("big_logo_lightsalmon.png", width=700)

st.markdown("<h6 style='text-align: center; color: grey;'>Nach welcher Produktkategorie suchst du?</h6>", unsafe_allow_html=True)
#st.write("")
st.image("product_category.png")

st.write("")

row1 = st.columns(3)
li_img = ["img04.png", "img02.png", "img03.png"]

for col, img in zip(row1, li_img): 
    with col:
      st.image(img)

st.write("")
st.markdown("<h6 style='text-align: center; color: grey;'>Wogegen suchst du ein Produkt?</h6>", unsafe_allow_html=True)
st.image("skin_problem.png")


st.image("img01.png")




































