# -*- coding: utf-8 -*-

import requests
from time import sleep as esperar
import json

tokenh = open('tokens.txt', 'r')
cvt = str(input('CONVITE: ')).strip()
idC = str(input('ID: ')).strip()


while True:
    for tokenn in tokenh.readlines():
        try:
            token = tokenn.strip()

            payload = {'content': '**hypn0thcy lindooo**'}

            headers = {'Authorization': token,'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.12 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36'}
            entrar = requests.post(f'https://discord.com/api/v8/invites/{cvt}', headers=headers)
            if entrar.status_code == 200:
                print(f'{token}   ->  SUCESSO ao entrar!')
            else:
                print(entrar.status_code)
                pass

            esperar(0.5)
            flood = r = requests.post(f'https://discord.com/api/v8/channels/{int(idC)}/messages', headers=headers, json=payload)

            if flood.status_code == 200:
                print(f'{token}   ->  SUCESSO no flood!') 
            else:
                print(flood.status_code)
                pass
        except Exception as ee:
            print(ee)
            pass
