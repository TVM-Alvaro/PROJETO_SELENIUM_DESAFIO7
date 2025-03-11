'''from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys
import random

def iniciar_driver():
    chrome_options = Options()
    # Fonte de opções de switches https://peter.sh/experiments/chromium-command-line-switches/

    arguments = ['--lang=pt-BR', '--window-size=800,1000',
                '--incognito']
    ''' Common arguments
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-us , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    for argument in arguments:
        chrome_options.add_argument(argument)

    caminho_padrao_para_download = 'E:\\Storage\\Desktop'

    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/32352ad08ee673a4d43e8593ce988b224f6482d3/chrome/common/pref_names.cc
    chrome_options.add_experimental_option("prefs", {
        'download.default_directory': caminho_padrao_para_download,
        # Atualiza diretório para diretório passado acima
        'download.directory_upgrade': True,
        # Setar se o navegar deve pedir ou não para fazer download
        'download.prompt_for_download': False,
        "profile.default_content_setting_values.notifications": 2,  # Desabilita notificações
        # Permite realizar múltiplos downlaods multiple downloads
        "profile.default_content_setting_values.automatic_downloads": 1,
    })

    driver = webdriver.Chrome(options=chrome_options)
    return driver


driver = iniciar_driver()
#função para digitar naturamente
def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)

#navegar até o desafio 07
driver.get('https://cursoautomacao.netlify.app/desafios')
# 1) Salvar nossa janela atual
janela_inicial = driver.current_window_handle 
print(f'primeira janela: {janela_inicial}')
# 2) Abrir um nova janela
driver.execute_script('window.scrollTo(0,2600);')
sleep(3)
botao_abrir_janela = driver.find_element(
    By.XPATH, "//button[text()='Abrir nova janela']")
sleep(1)
# quando se trata de botao para clicar e abrir uma nova janela executar esse comando ao inves do click
driver.execute_script('arguments[0].click()', botao_abrir_janela) 
sleep(1)
# 3) quais janelas estão abertas
janelas = driver.window_handles
for janela in janelas:
    print(janela)
    if janela not in janela_inicial:
        # alterar para essa nova janela
        texto = 'Esse curso é nota 1000'
        driver.switch_to.window(janela)
        sleep(2)
        campo_opiniao = driver.find_element(By.ID, "opiniao_sobre_curso")
        sleep(2)
        #campo_opiniao.send_keys('Esse curso é nota 1000')
        digitar_naturalmente(texto,campo_opiniao)
        sleep(2)
        driver.execute_script('window.scrollTo(0,2600);')
        botao_pesquisar = driver.find_element(By.ID, "fazer_pesquisa")
        sleep(2)
        botao_pesquisar.click()
        sleep(3)
        driver.close()
#voltar para janela inicial
driver.switch_to.window(janela_inicial)

#Escrever no campo do desafio 7

texto2 = 'mestre da automação'

campo_desafio7 = driver.find_element(By.ID, "campo_desafio7")
sleep(1)
digitar_naturalmente(texto2,campo_desafio7)
sleep(1)

input('')
driver.close()