import requests
import pandas as pd
from pandas import read_excel

"""
@description Classe de Entrega, responsável por definir como o objeto será enviado.
"""
class Entrega():
    def __init__(self, itemEntrega, produto, endereco, cep, complemento):
        self.itemEntrega = itemEntrega
        self.produto = produto
        self.endereco = endereco
        self.cep = cep
        self.complemento = complemento

"""
@description Responsável por identificar os campos e 
enviar a requisição para o Google Forms.
@param {entrega} objeto do tipo Entrega
@return {void}
"""
def send_request(entrega):
    url = "https://docs.google.com/forms/d/e/1FAIpQLSeGkKoum1HEonSxWeZP8r2PDHBncBVxRn61O4x4SwgTILDWtQ/formResponse"

    data = {
        "entry.796078177"  : "Monica Maria Wanderley Padilha",
        "entry.1739664412" : entrega.itemEntrega,
        "entry.1391419047" : entrega.cep,
        "entry.377666364"  : entrega.endereco,
        "entry.2057892184" : entrega.complemento
    }

    print(data)
    result = requests.post(url, data)

    print(result)

"""
@description Responsável por ler o excel .xlsx e 
montar o objeto Entrega para ser enviado.
@param {filename} caminho relativo do arquivo com o nome do arquivo 
@return {void}
"""
def excel_file(filename):
    pd.set_option("display.max_rows", 1000)
    pd.set_option("display.max_columns", 10)

    data = pd.read_excel(filename + ".xlsx", 0)

    for i in range(data.shape[0]):
        itemEntrega = data.iloc[i]["Item de entrega"]
        produto     = data.iloc[i]["Produto"]
        cep         = data.iloc[i]["CEP"]
        endereco    = data.iloc[i]["Endereço"]
        complemento = data.iloc[i]["Complemento"]

        entrega = Entrega(itemEntrega, produto, endereco, cep, complemento)
        send_request(entrega)

"""
@description Classe Main, responsável pelo start da aplicação
"""
def main():
    filename = input("Caminho e o Nome da planilha (ex: ~/Desktop/automacao):\n")
    excel_file(filename)

main()

