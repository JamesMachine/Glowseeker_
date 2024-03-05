import streamlit as st

from utils import get_colors_from_style
from settings import INGREDIENTS

st.set_page_config(
    page_title="Glowseeker", page_icon="🖼️", initial_sidebar_state="collapsed"
)

st.markdown("<h1 style='text-align: center; color: grey;'>Recommendations</h1>", unsafe_allow_html=True)


st.write("")
form = st.form(key="form_settings")
col1, col2, col3 = form.columns([3, 1, 1])

product = col1.text_input(
    "Do you have a particular product in mind that you're looking for?",
    key="product",
)

age_range = col2.slider(
    "Age Range",
    0,
    100,
    key="age_range",
)

ingredient = col3.selectbox(
    "Ingredients",
    options=INGREDIENTS,
    key="ingredients",
)

expander = form.expander("Advance Search")
col1style, col2style, _, col3style = expander.columns([2, 2, 0.1, 1])

######

allergic_options = ["Yes", "No", "Don't' know"]
allergy = col1style.radio(
    "Are you allergic to anything?",
    options=allergic_options,
    key="allergy",
)

skintype_options = ["Dry", "Oily", "Neutral"]
skintype = col1style.radio(
    "Skin Type",
    options=skintype_options,
    key="skintype",
)

skin_color = col1style.color_picker(
    "Skin Color",
    key="skin_color",
)

price_range = col1style.slider(
    "Price Range",
    min_value=0,
    max_value=10000,
    help="How much do you want to invest on yourself today?",
    key="price_range",
)

form.form_submit_button(label="Submit")


# form.form_submit_button(label="Submit")


