import pandas as pd
from pandas import read_excel

def excel_file():
    pd.set_option("display.max_rows", 1000)
    pd.set_option("display.max_columns", 10)

    data = pd.read_excel("automacao.xlsx", "Planilha1")

    for name, sheet in data.items():
        print(sheet)

excel_file()
