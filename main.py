import streamlit as st
from grammarToLanguage import generar_gramatica

st.title("Generador de lenguajes")

cols = st.columns(2)

with cols[0]:
    st.subheader("Terminales (vt)")
    vt_input = st.text_input("Ingrese los símbolos terminales separados por comas", "a,b")
    vt = set(elemento.strip() for elemento in vt_input.split(","))
with cols[1]:
    st.subheader("No Terminales (vn)")
    vn_input = st.text_input("Ingrese los símbolos no terminales separados por comas", "S,A")
    vn = set(elemento.strip() for elemento in vn_input.split(","))

st.subheader("Producciones (p)")
st.text("separar sibolos de las producciones por espacios")
p = {}
for simbolo in vn:
    # Eliminamos los valores predeterminados específicos
    producciones = st.text_input(f"Producciones para {simbolo} (separadas por '|')")
    p[simbolo] = producciones.split("|")

# Entrada para profundidad máxima
max_profundidad = st.slider("Profundidad máxima", 1, 10, 5)

if st.button("Generar cadenas"):
    gramatica = (vt, vn, p)
    try:
        cadenas = generar_gramatica(gramatica=gramatica, max_profundidad=max_profundidad)
        st.subheader("Cadenas generadas:")
        for cadena in sorted(cadenas, key=len):
            st.write(f"- {cadena}")

    except ValueError as e:
        st.error(f'Error: {e}')