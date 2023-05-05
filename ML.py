import requests
import pandas as pd
import time
import os

client_id = 'seu_client_id'
client_secret = 'seu_client_secret'

while True:
    # Obtenha um token de acesso
    url = 'https://api.mercadolibre.com/oauth/token'
    data = {'grant_type': 'client_credentials', 'client_id': client_id, 'client_secret': client_secret}
    response = requests.post(url, data=data)
    access_token = response.json()['access_token']

    # Faça a chamada à API de Relatórios do Mercado Livre
    url = 'https://api.mercadolibre.com/orders/reports/search'
    params = {'access_token': access_token, 'date_created.from': '2022-01-01T00:00:00.000-00:00', 'date_created.to': '2022-01-31T23:59:59.000-00:00'}
    response = requests.get(url, params=params)
    report_json = response.json()

    # Transforme o JSON em um dataframe pandas
    report_df = pd.DataFrame(report_json['results'][0]['content'])

    # Salve o dataframe em formato CSV
    report_df.to_csv('report.csv', index=False)

    # Carregue o arquivo CSV como um dataframe pandas e remova a primeira linha
    report_df = pd.read_csv('report.csv', skiprows=1)

    # Salve o dataframe em formato XLS e substitua o arquivo existente
    report_df.to_excel('report.xls', index=False, mode='w')

    # Abra o arquivo XLS
    os.startfile('report.xls')

    # Aguarde 60 segundos antes da próxima atualização
    time.sleep(60)
