import streamlit as st
import pandas as pd
from src.authentication import show_authenticator

show_authenticator()

st.title('Upload de Arquivo e Exibição de Tabela')

uploaded_file = st.file_uploader("Escolha um arquivo CSV ou Excel", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    
    st.write("Tabela de Dados:")
    st.dataframe(df)