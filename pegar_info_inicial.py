from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.edge.service import Service

from time import sleep

import pandas as pd

def pegar_informacoes_de_professores(text):
    campos = text.split('\n')
    informacoes = {}
    
    informacoes['Nome'] = campos[0].strip()
    for campo in campos:
        if 'Unidade' in campo and 'de Lotação' not in campo:
            informacoes['Unidade'] = campo.split(':')[1].strip()
        if 'Unidade de Lotação' in campo:
            informacoes['Unidade de Lotação'] = campo.split(':')[1].strip()
        if 'Regime' in campo:
            informacoes['Regime'] = campo.split(':')[1].strip()

    return informacoes

CAMINHO_EDGE_DRIVER = 'C:/Dados/edgedriver_win64_128/msedgedriver.exe' #Para versão edge 126.0.2592.87 

service = Service(executable_path=CAMINHO_EDGE_DRIVER)
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)

wait = WebDriverWait(driver, 30)
lista_de_informacoes = []

for i in range(0,339):
    driver.get(f'https://unesp.br/portaldocentes/docentes;jsessionid=F21FD113E3A12E6C0E76DB3601671A16?page={i}&inicial=')
    sleep(6)

    professores = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.col-sm-7')))

    for professor in professores:
        try:
            link = professor.find_element(By.CSS_SELECTOR, 'a.lattes-link').get_attribute('href')
        except:
            link = 'Não possui lattes'

        informacoes_professor = {}
        informacoes_professor = pegar_informacoes_de_professores(professor.text)
        informacoes_professor['Lattes'] = link
        lista_de_informacoes.append(informacoes_professor)

        print(informacoes_professor)
        print(20 * '=')

df = pd.DataFrame(lista_de_informacoes)
df.to_csv('info_docentes.csv', encoding='latin-1')