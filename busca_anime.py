#!/usr/bin/python3
# Bibliotecas necessárias para pesquisar a lista dos animes em um site
from bs4 import BeautifulSoup
import requests
# Bibliotecas necessárias para enviar os alertas por wats
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

# Precisa configurar algumas coisas antes de utilizar a biblioteca selenium
# Se não tiver, baixar o webdriver. Eu utilizei o driver do firefox (https://github.com/mozilla/geckodriver/releases)
# Descompacte o arquivo no diretório /usr/bin
# Se acontecer de o driver bloquear a sua conexão, abra o arquivo hosts em /etc/hosts
# Acrescente o segunte texto "192.0.0.1 localhost" sem aspas

navegador = webdriver.Firefox()
navegador.get("https://web.whatsapp.com/")

animes = open("animes.txt", "r")

URL = open("site.txt","r")
html = requests.get(URL.read())
soup = BeautifulSoup(html.content, "html.parser")

lancamentos = []
# Acontece algum bug na comparaçao
for titulo in soup.find_all(class_="title"):
    for nome in animes:
        if nome in str(titulo):
            lancamentos.append(nome)

# Envia um zap com os animes lançados
# OBS: O botão de submit não está funcioando 
numero = "XXXXXXXXXX"
texto = f"Animes lançados hoje {lancamentos}"
link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
navegador.get(link)
navegador.find_element("xpath", "//button[@type='submit']").click()