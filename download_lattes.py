import pandas as pd
import pyautogui as bot 
import os
from unicodedata import normalize

CAMINHO_PASTA_LATTES = 'C:/Users/João Tinti/Downloads/'
dados_professores = pd.read_csv('info_docentes.csv', encoding='latin-1')
for nome_professor, link_lattes in zip(dados_professores['Nome'], dados_professores['Lattes']):
    nome_professor = normalize('NFKD', nome_professor).encode('ASCII', 'ignore').decode('ASCII')
    
    if 'Não possui lattes' in link_lattes:
        continue
    else:
        if f'{nome_professor}_lattes.html' not in os.listdir(CAMINHO_PASTA_LATTES):
            print(f'Baixando o lattes de {nome_professor}')
            bot.press('win')
            bot.sleep(4)
            bot.write('Chrome')
            bot.sleep(4)
            bot.press('enter')
            bot.sleep(4)
            bot.write(link_lattes)
            bot.sleep(4)
            bot.press('enter')
            bot.sleep(60)
            bot.click(x=1058, y=548) #Clica em "Submeter"    
            bot.sleep(40)
            bot.hotkey('ctrl', 'u')
            bot.sleep(5)    
            bot.hotkey('ctrl', 's')
            bot.sleep(4)
            bot.write(f'{nome_professor}_lattes')
            bot.sleep(4)
            bot.press('enter')
            bot.sleep(4)
            bot.hotkey('alt', 'f4')
            bot.sleep(4)

        else:
            print(30 * '=')
            print(f'O lattes de {nome_professor} já foi baixado')
            print(30 * '=')
