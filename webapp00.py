# MEU PRIMEIRO WEB APP
import streamlit as st
import requests
from io import BytesIO
import pandas as pd

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Dashboard Teste")
st.header("Grupo Murilo & Colegas")

urlCSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQruiuZivFX_wDz-2aFue5__5Wu0ua6gZHU77lNNEUb2IUhx0MExIKzvfjBFFDUP-awXC8rKoX7LXEQ/pub?output=csv"
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
st.write(df.head(3))

st.title("Valores Médios: ")
st.title(f"Valor 1: {df['Valor1'].mean()}")
st.title(f"Valor 2: {df['Valor2'].mean()}")
