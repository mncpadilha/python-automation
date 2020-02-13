import pandas as pd
from pandas import read_excel

def send_response(entrega):
    url_test = "https://docs.google.com/forms/d/e/1FAIpQLSfc5gkEAHvXB9zSZYHUewj466yhpE2_hf7r1JzJYu088VgIzA/formResponse"
    url_def = "https://docs.google.com/forms/d/e/1FAIpQLSeGkKoum1HEonSxWeZP8r2PDHBncBVxRn61O4x4SwgTILDWtQ/formResponse"

    data = {
        "entry.11703947"   : "Monica Maria Wanderley Padilha",
        "entry.283002341"  : "Item Entrega",
        "entry.96278573"   : "CEP",
        "entry.1587431302" : "Endereço",
        "entry.1495180370" : "Complemento"
    }

    print(data)
    result = requests.post(url_test, data)

    print(result)

def excel_file():
    pd.set_option("display.max_rows", 1000)
    pd.set_option("display.max_columns", 10)

    data = pd.read_excel("automacao.xlsx", "Planilha1")

    for name, sheet in data.items():
        print(sheet)

excel_file()
