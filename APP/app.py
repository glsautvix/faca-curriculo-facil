import streamlit as st

class AppRunner:
    def __init__(self):
        pages = {
            "USER": [
            st.Page("screens/create_curriculo.py",),
            st.Page("screens/home.py"),
            ],
            "Configuração": [
            st.Page("screens/options.py"),
            st.Page("screens/help.py"),]
            ,
        }

        pg = st.navigation(pages)
        pg.run()



a = AppRunner()
