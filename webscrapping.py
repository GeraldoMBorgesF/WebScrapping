from bs4 import BeautifulSoup

import requests

# objeto site recebendo o conteudo da requisição http do site referente à url
site = requests.get("https://blog.nubank.com.br/tabela-do-imposto-de-renda-2022/").content

# objeto soup baixa o código fonte do site
soup = BeautifulSoup(site, 'html.parser')

# prettify transforma o código fonte em string e o imprime
# print(soup.prettify())

busca =soup.find_all("tr")

# print(soup("title"))

print(busca)

#Desenvolvendo um Web Scrapping . Aula DIO: Segurança da informação com Python