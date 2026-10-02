import streamlit as st

st.title("🚌 Expresso Mobilidade - Painel do Operador")

nome = st.text_input("Digite seu nome:")
if nome:
    st.write("Olá,", nome, "! Bem-vindo ao painel de operações.")

linha = st.selectbox(
    "Escolha uma linha prioritária:",
    ["510", "520", "550"]
)
st.write("Linha selecionada:", linha)

horarios = {
    "510": "06:00 | 06:30 | 07:00 | 07:30",
    "520": "06:15 | 06:45 | 07:15 | 07:45",
    "550": "05:50 | 06:20 | 06:50 | 07:20",
}
st.write("Próximos horários:", horarios[linha])

linhas = st.multiselect(
    "Escolha as linhas para o relatório de passageiros:",
    ["510", "520", "550", "620"]
)
st.write("Linhas escolhidas:", linhas)

if st.button("Calcular"):
    if linhas:
        st.write("Calculando demanda e distribuição de frota...")
        for l in linhas:
            st.write("Linha", l, "-> 3 ônibus alocados (simulação)")
        st.write("Cálculo concluído!")
    else:
        st.write("Selecione ao menos uma linha para calcular.")
