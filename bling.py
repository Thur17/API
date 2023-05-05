from blingapi import Api
import pandas as pd
import time

api = Api(api_key="SUA_CHAVE_DA_API_DO_BLING")

while True:
    response = api.get_report(report_type="produtos")
    if response.status_code == 200:
        with open("produtos.csv", "wb") as f:
            f.write(response.content)
        print("Base de dados baixada com sucesso.")
        df = pd.read_csv("produtos.csv")
        df.to_excel("produtos.xls", index=False)
        print("Arquivo XLS gerado com sucesso.")
    else:
        print("Falha ao baixar a base de dados.")
    time.sleep(60)  # Espera 1 minuto antes de baixar a próxima base de dados
