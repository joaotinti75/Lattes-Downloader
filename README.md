# Lattes-Downloader
Scripts em Python para automatizar o download de currículos Lattes, facilitando a coleta de dados para análises acadêmicas e científicas.

## Etapas para realizar o download dos currículos lattes de cada professor

### 1	– Obtenção dos links do lattes de cada professor da UNESP

Para obtenção dos nomes e links dos currículos lattes de cada professor da UNESP, o site oficial da universidade foi utilizado (https://unesp.br/portaldocentes). Foram contabilizados 3.383 currículos, e suas informações foram salvas em um arquivo CSV.

O script `pegar_info_inicial.py` realiza essa etapa de obtenção dos links.

### 2	– Download do lattes em HTML de cada professor

Após obtenção dos links dos currículos lattes, um outro script python foi desenvolvido utilizando as bibliotecas PyAutogui e Selenium, no intuito de realizar o download dos currículos de cada professor. A extensão "NopeCHA:CAPTCHA Solver" foi utilizada para realização dos CAPTCHAS da página. Dos 3.383 currículos, apenas 1.068 currículos foram baixados, devido às restrições de acesso impostas pela plataforma lattes. Os currículos foram salvos como HTML.

O script `download_lattes.py` é responsável pela realização do download dos currículos.

### 3	– Criação do banco de dados estruturado utilizando expressões regulares

Após efetuar o download dos 1.068 currículos lattes, um script python foi desenvolvido utilizando expressões regulares para realizar a extração das informações mais relevantes de cada currículo, como nome do professor, resumo, foto do professor e linhas de pesquisa. Após extração, o script estrutura essas informações em um arquivo JSON. 

O script `extrair_info_oficial_com_re.py` é responsável pela extração dessas informações dos currículos.

## Observação
Este trabalho foi realizado para a disciplina de “Aprendizado Profundo” do Programa de Pós-Graduação em Ciência da Computação (PPGCC) da Unesp, ministrada pelo Prof. Dr. Denis Henrique Pinheiro Salvadeo.
