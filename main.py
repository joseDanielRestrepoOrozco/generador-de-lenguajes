import streamlit as st

st.title("Generador de lenguaje")
st.text("Bienvenido al generador de lenguajes formales")

vt = st.text_input("simbolos terminales")

vn = st.text_input("simbolos no terminales")

s = st.text_input("Simbolo no terminal de inicio")

p = st.text_input("caminos")
