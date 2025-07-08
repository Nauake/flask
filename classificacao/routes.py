from classificacao import app
from flask import render_template, url_for, request
import pandas as pd



@app.route("/")
def home():
    path = r"C:\Users\Auhelbiton\OneDrive\Documentos\Classificacao_Infa.xlsx"
    dados = pd.read_excel(path, skiprows=1, usecols=range(8))
    nomes = dados['NOME'].tolist()
    nomes.insert(0, "TODOS OS NOMES")

    return render_template('index.html', nomes=nomes, dados=dados)

