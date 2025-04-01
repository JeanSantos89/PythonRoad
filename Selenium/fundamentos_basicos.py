from selenium import webdriver #sempre necessário importar para automação de tarefas
import time #importar biblioteca time para quando quiser que o chrome "espere". Se mantenha aberto.

# abrir navegador
navegador = webdriver.Chrome()

# acessar um site
navegador.get("https://www.youtube.com/")
# deixar em tela cheia
navegador.maximize_window()



time.sleep(10) # Quando quiser que o chrome "espere". Se mantenha aberto.




# Biblioteca - Selenium Python