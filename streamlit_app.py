import streamlit as st
import pandas as pd
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    "How do i started the dataset in my rep"
)
df = pd.read_csv('partos-e-cesarianas.csv', sep=';', on_bad_lines='skip')
print(df.head())  # Analise os dados para inconsistências
df.columns = df.columns.str.strip()

# Verificar e limpar dados inválidos
df = df.dropna(subset=['Nº Total de Partos'])  # Remove linhas com valores NaN

# Exibir o gráfico
st.line_chart(df['Nº Total de Partos'])

