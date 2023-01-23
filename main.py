import pandas as pd
import os
from twilio.rest import Client

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']


def enviarMsg(text):
    account_sid = '32131244431'
    auth_token = '312312321'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=text,
                        from_='+890809808',
                        to='+989809800'
                    )
    print(message)


for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'files\{mes}.xlsx')

    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']
                                     > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']
                                   > 55000, 'Vendas'].values[0]
        enviarMsg(f'O guri {vendedor} da silva vendeu R$ {vendas } ')
