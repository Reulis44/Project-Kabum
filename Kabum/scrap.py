# Importações das libs
from time import sleep

import pandas as pd
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Robo:

    def __init__(self) -> None:
        self.configs()
        self.acessando_site_kabum()
        self.acessando_etapa_pc_gamer()
        self.captando_nomes_dos_produtos()


    def configs(self):
        # Configurações do Driver
        self.servico = Service(ChromeDriverManager().install())
        self.site = webdriver.Chrome(service=self.servico)
        # Configurações da planilha
        self.arquivo = load_workbook(filename="C:\\Users\\Alan\\Desktop\\Projetos GIT pessoal\\Project-Kabum\\Kabum\\Produtos.xlsx")
        self.planilha = self.arquivo["Produtos"]

    
    def acessando_site_kabum(self):
        self.site.get('https://www.kabum.com.br/')
        sleep(5)

    
    def acessando_etapa_pc_gamer(self):
        self.site.find_element(By.ID, 'promocaoPcGamerMenuSuperior').click()
        sleep(5)
    

    def captando_nomes_dos_produtos(self):
      self.nome_produto = self.site.find_elements(By.CSS_SELECTOR, "[class='sc-d99ca57-0 iRparH sc-ff8a9791-16 kRYNji nameCard'")
      self.valor = self.site.find_elements(By.CSS_SELECTOR, "[class='sc-3b515ca1-2 jTvomc priceCard']")
      for c in self.nome_produto:
        ...
      for b in self.valor:
        self.produto = [(c.text, b.text)]
        for d in self.produto:
          self.planilha.append(d)
      try:
        self.botao = self.site.find_element(By.CSS_SELECTOR, "[class='next']")
        if self.botao:
            self.botao.click()
            sleep(5)
            self.captando_nomes_dos_produtos()
      except:
        print("Sem novas paginas. Finalizando script.")
        self.arquivo.save("C:\\Users\\Alan\\Desktop\\Projetos GIT pessoal\\Project-Kabum\\Kabum\\Produtos.xlsx")

Robo()
