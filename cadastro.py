import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

s = Service("./driver")

ChromeOptions = Options()
ChromeOptions.headless = False
driver = webdriver.Chrome(service=s, options=ChromeOptions)

def cadastro(nome, sobrenome, email):
    driver.get("http://127.0.0.1:59352/")
    print('Iniciando driver')
    time.sleep(1)
    campo_nome = driver.find_element(by=By.NAME, value="name")
    campo_nome.click()
    time.sleep(1)
    campo_nome.send_keys(nome)
    campo_sobrenome = driver.find_element(by=By.NAME, value="surname")
    campo_sobrenome.click()
    time.sleep(1)
    campo_sobrenome.send_keys(sobrenome)
    campo_email = driver.find_element(by=By.NAME, value="email")
    campo_email.click()
    time.sleep(1)
    campo_email.send_keys(email)
    campo_enviar = driver.find_element(by=By.CLASS_NAME, value="botao-enviar")
    campo_enviar.click()
    time.sleep(2)

    driver.get("http://127.0.0.1:59352/enviado.html")
    search_results = driver.find_elements("css selector", "h3")
    for result in search_results:
        print(result.text)

cadastro("Lucas", "Pereira", "lucas.pereira@gmail.com")
cadastro("Isabella", "Santos", "isabella.santos@gmail.com")
cadastro("Thiago", "Oliveira", "thiago.oliveira@example.com")
