from selenium import webdriver  # importar as dependências, como a biblioteca Selenium para simular o navegador
from selenium.webdriver.common.keys import Keys # biblioteca keys para simular a escrita de caracteres em um input
import time # biblioteca time para simular o tempo de uma ação para outra

browser = webdriver.Chrome() # Caminho da excecução do webDriver

browser.get('https://www.ts3.lu/login.php') # metodo get para abrir um navegador e entrar na URL passada como parametro
time.sleep(5)

elem = browser.find_element_by_name('username')  # Pega um elemento input em HTML pelo nome
elem.send_keys('seu-login-no-site') # Escreve o nome do seu usuário (Login ) nesse input

elem = browser.find_element_by_name('password') # Pega um elemento password do tipo input por nome
elem.send_keys('sua-senha') # Os caracteres de sua senha é passado como um parametro para ser digitada em um input

entrar = browser.find_element_by_name('loginBtn') # Pega o elemento do botão submit "Entrar"
entrar.click() # Clica no elemento solicitado pela instrução anterior
time.sleep(3) # biblioteca para simular segundos de uma ação para outra

buttonAdministrator = browser.find_element_by_xpath('//*[@id="main-menu"]/li[4]/a') # Pega o xPath de um elemento da página: Botão administrador
buttonAdministrator.click()
time.sleep(3) # simulação para clicar nesse elemento

box = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/table[1]/tbody/tr/td[1]/input') # Pega um elemento do type checkBox da página
box.click() # simulação para clicar nesse elemento

renovar = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/table[2]/thead/tr/th[2]/input') # Pega o xPath de um elemento da página: button renovar
renovar.click()
time.sleep(10) # Espera 10 segundos, pois o próximo elemento é do tipo Hidden

renovarGratis = browser.find_element_by_name('renovargratis') # Finaliza clicando em Renovar (enviar ) para que a renovação do servidor seja feita
renovarGratis.click()
time.sleep(15) 

browser.close() # Após 15 segundos definidos na instrução acima, o browser fechará, terminando a execução do BOT
# ou browser.quit()
