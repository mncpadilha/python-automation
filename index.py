import pandas as pd
from pandas import read_excel

class Entrega():
    def __init__(self, itemEntrega, produto, endereco, cep, complemento):
        self.itemEntrega = itemEntrega
        self.produto = produto
        self.endereco = endereco
        self.cep = cep
        self.complemento = complemento

def send_response(entrega):
    url = "https://docs.google.com/forms/d/e/1FAIpQLSeGkKoum1HEonSxWeZP8r2PDHBncBVxRn61O4x4SwgTILDWtQ/formResponse"

    data = {
        "entry.796078177"  : "Monica Maria Wanderley Padilha",
        "entry.1739664412" : entrega.itemEntrega,
        "entry.1391419047" : entrega.cep,
        "entry.377666364"  : entrega.endereco,
        "entry.2057892184" : entrega.complemento
    }

    print(data)
    result = requests.post(url_test, data)

    print(result)

def excel_file(filename):
    pd.set_option("display.max_rows", 1000)
    pd.set_option("display.max_columns", 10)

    data = pd.read_excel(filename + ".xlsx", 0)

    for name, sheet in data.items():
        print(sheet)

def main():
    filename = input("Caminho e o Nome da planilha (ex: ~/Desktop/automacao):\n")
    excel_file(filename)

main()

