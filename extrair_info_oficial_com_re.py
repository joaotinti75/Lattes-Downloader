import re
import os 
import json 

def get_resumo(html):
    regex = r'resumo</span>"&gt;</span>(.*?)<span class="html-tag">'

    resultado = re.search(regex, html, re.DOTALL)

    if resultado:
        texto_extraido = resultado.group(1)
        texto_extraido = texto_extraido.replace('&amp;#10;', ' ')
        return texto_extraido 
    else:
        return None
    
def get_foto(html):
    regex = r'http://servicosweb\.cnpq\.br/wspessoa/servletrecuperafoto\?tipo=1&amp;id=(.*?)">'

    resultado = re.search(regex, html)

    if resultado:
        texto_extraido = resultado.group(1).strip()  # Remove espaços desnecessários (se houver)
        texto_extraido = texto_extraido.split(" ")[0][:-1]
        return f'http://servicosweb.cnpq.br/wspessoa/servletrecuperafoto?tipo=1&id={texto_extraido}'
    else:
        return None

def get_linha_de_pesquisa(html):
    regex = r'rel="noreferrer noopener">#LP_(.*?)</a>'

    resultado = re.findall(regex, html)

    if resultado:

        return resultado
    else:
        return None


CAMINHO_PASTA_CURRICULOS = 'C:/Dados/PROJETO_DL/Curriculos_Parciais'
dicionario_professores = {}

for curriculo in os.listdir(CAMINHO_PASTA_CURRICULOS):
    nome_professor = curriculo.split('_lattes')[0]
    print(100 * '-')
    print(f'Extraindo informações de {nome_professor}')
    print('')
    print('')

    dicionario_professores[nome_professor] = {}

    #Abrindo o primeiro currículo
    with open(os.path.join(CAMINHO_PASTA_CURRICULOS, curriculo), 'r', encoding="ISO-8859-1") as file:
        html_content = file.read()

    resumo_resultado = get_resumo(html_content)
    dicionario_professores[nome_professor]['resumo'] = resumo_resultado
    print('RESUMO: ', resumo_resultado)
    print('')
    print('')

    link_foto = get_foto(html_content)
    dicionario_professores[nome_professor]['foto'] = link_foto
    print('LINK FOTO: ', link_foto)
    print('')
    print('')

    linhas_de_pesquisa = get_linha_de_pesquisa(html_content)
    dicionario_professores[nome_professor]['linhas_pesquisa'] = linhas_de_pesquisa
    print('LINHAS DE PESQUISA: ', linhas_de_pesquisa)
    print('')
    print('')

#Convertendo a saída para um JSON
with open("curriculos_parciais.json", "w", encoding ='latin-1') as outfile: 
    json.dump(dicionario_professores, outfile, ensure_ascii = True)