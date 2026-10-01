import streamlit as st
import pandas as pd

nome = "Gabriela Coelho"
idade = 17

st.write("Meu primeiro dash")
st.subheader(nome)

st.write("nome:", nome, "idade:", idade)
st.write("Olá, mundo!!")

df = pd.DataFrame({
    'Matéria': ['Português', 'Matemática', 'Python', 'FrameWork'],
    'Nota': [5, 9, 7, 10]
})

st.write(df)