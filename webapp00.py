# MEU PRIMEIRO WEB APP
import streamlit as st
import requests
from io import BytesIO
import pandas as pd

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Teste")
st.header("TCC ISAQUE E RAHAL")

urlCSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSVj0iXQ8PdpQ4qQ6wpM8rjWqHy4a39SP6eYRgShS41DioSHbYuvMnoRSNOKVAzoKLcft1cTeMkisct/pub?gid=1162276461&single=true&output=csv"
rD = requests.get(urlCSV)
dataD = rD.content
db = pd.read_csv(BytesIO(dataD))
db.columns = ["DataHora", "Field1", "Field2"]

def remove_str_start_end(s, start, end):
    resp = s[:start] + s[end + 1:]
    return float(resp)

valor1 = []
valor2 = []
for i in range(len(db)):
    valor1.append(remove_str_start_end(db["Field1"][i], 0, 1))
    valor2.append(float(db["Field2"][i]))

df = {'TimeStamp': db['DataHora'], 'Valor1': valor1, 'Valor2': valor2}
df = pd.DataFrame(df)
st.write(df)

st.title("Valores Médios: ")
col1, col2 = st.columns(2)
with col1:
    #st.title(f"Valor 1: {df['Valor1'].mean()}")
    st.metric(label="Valor 1", value=df['Valor1'].mean(), delta=0.0, delta_color="inverse")
with col2:
    #st.title(f"Valor 2: {df['Valor2'].mean()}")
    st.metric(label="Valor 1", value=df['Valor2'].mean(), delta=0.0, delta_color="inverse")
