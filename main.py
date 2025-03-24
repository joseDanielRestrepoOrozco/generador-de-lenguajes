import streamlit as st
from grammarToLanguage import generar_gramatica

# Título de la aplicación
st.title("Generador de Gramáticas")

# Entrada para terminales (vt)
st.subheader("Terminales (vt)")
vt_input = st.text_input("Ingrese los símbolos terminales separados por comas", "a,b")
vt = set(vt_input.split(","))

# Entrada para no terminales (vn)
st.subheader("No Terminales (vn)")
vn_input = st.text_input("Ingrese los símbolos no terminales separados por comas", "S,A")
vn = set(vn_input.split(","))

# Entrada para producciones (p)
st.subheader("Producciones (p)")
p = {}
for simbolo in vn:
    producciones = st.text_input(f"Producciones para {simbolo} (separadas por '|')",
                                 value="a S b|A" if simbolo == "S" else "a A|b")
    p[simbolo] = producciones.split("|")

# Entrada para profundidad máxima
max_profundidad = st.slider("Profundidad máxima", 1, 10, 5)

# Botón para generar las cadenas
if st.button("Generar cadenas"):
    gramatica = (vt, vn, p)

    try:
        cadenas = generar_gramatica(gramatica, max_profundidad=max_profundidad)

        st.subheader("Cadenas generadas:")

        # Mostrar las cadenas como una lista
        for cadena in sorted(cadenas):
            st.write(f"- {cadena}")

    except ValueError as e:
        st.error(f'Error: {e}')