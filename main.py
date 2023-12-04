import streamlit as st

from web_functions import load_data

from Tabs import home, data, predict, visualise

st.set_page_config(
    page_title='SleepEmoStress Analyzer',
    page_icon='heavy_exclamation_mark',
    layout='wide',
    initial_sidebar_state='auto'
)

Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    "Visualisation": visualise
}

st.sidebar.title("Navigation")

page_icons = {
    "Home": "🏠",
    "Data Info": "ℹ️",
    "Prediction": "🔮",
    "Visualisation": "📊"
}

selected_page = st.sidebar.selectbox("Select Page", [f"{value} {key}" for key, value in page_icons.items()])

page = selected_page.split(" ", 1)[1]


df, X, y = load_data()

if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif page == "Data Info":
    Tabs[page].app(df)
else:
    Tabs[page].app()
