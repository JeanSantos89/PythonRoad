from selenium import webdriver #sempre necessário importar para automação de tarefas
import time #importar biblioteca time para quando quiser que o chrome "espere". Se mantenha aberto.

# abrir navegador
navegador = webdriver.Chrome()

# acessar um site
navegador.get("https://www.youtube.com/")

# deixar em tela cheia
navegador.maximize_window()

# achar um elemento na tela. procura pelo elemento por trás no HTML (classe, id, etc) - Procuar em documentação Selenium em caso de dúvida 
pesquisar = navegador.find_element("class name", "ytSearchboxComponentInput yt-searchbox-input title")
# em caso de existir várias classes com o mesmo nome, será selecionado a primeira que achar, então:

#
#lista_pesquisar = navegador.find_element("class name", "ytSearchboxComponentInput yt-searchbox-input title")
# Agora possuo uma lista com todos os elementos com a mesma classe
# Se eu quiser achar um específico, com texto específico ou outras funcionalidades:

#for elemento in lista_pesquisar: # Procuro um texto presente no elemento que desejo, se tiver, eu executo o que quiser, após isso, break.
    if "pesquisar texto" in elemento.text:
        elemento.click()
        break


# gerenciar abas
#abas = navegador.window_handles # se 2 abas abertas, defino as abas = [0,1]
#navegador.switch_to.window(abas[1]) # Se por exemplo, a aba 0 era a principal, eu adiciono esse código e torno a segunda aba como a principal agora.


# escrever em formularios

#1. Achar o elemento
#form = navegador.find_element("id", "exemplo")
#form.send_keys("texto que você quer) # Não precisa uma variavel para tudo, mas é útil.

#2. Clicar no elemento, ENVIAR por exemplo

#navegador.find_element("id","BOTAO ENVIAR").click() # SE ele não estiver aparecendo na tela, ele não IRA EXECUTAR. PRECISA ESTAR APARECENDO NA TELA

#3. Scrollar
#navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", variavel_elemento_que_quero_achar)
# Passei um argumento [0] onde a primeira variavel que eu passar, é o que ele vai scrollar até achar. E deixa centralizado na tela.


######## ------- ESPERA MANUAL, 1º OPÇÃO
# Se for dinamico e precisa esperar a tela "carregar" para eu executar, apenas adiciono um:
#time.sleep(x segundos) # antes da execução que quero, por exemplo clicar
#pesquisar.click()

######## ------- ESPERA DINAMICA, 2º OPÇÃO
#from selenium.webdriver.support.ui import webDriverWait 
#from selenium.webdriver.support import expected_conditions as EC 
##### duas importações para ele mandar esperar algo (L54) que é esperado acontecer (L55)

#espera = webDriverWait(navegador, 10) # esperar algo acontecer, depois disso ele só tenta continuar ---- CONDIÇÃO
#espera.until(EC.element_to_be_clickable(botao que quero clicar ou coisa assim)) # aqui eu vou executar apenas quando o elemento que eu quero seja clicavel. Se demorar mais que o tempo (L58) - 10 segundos, irá seguir o código independente ---- CONDIÇÃO
#botao que quero clicar.click() ## Ele executa após as condições
##### TUDO INTERLIGADO, DINAMICO


# clicar no elemento
pesquisar.click()

time.sleep(10) # Quando quiser que o chrome "espere". Se mantenha aberto.

#Sempre espera o site carregar total para acontecer a próxima ação. 
