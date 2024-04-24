from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import time

def get_filmes():

    urlPage = "https://pt.wikipedia.org/wiki/Lista_do_BFI_com_os_50_filmes_que_voc%C3%AA_deveria_ver_at%C3%A9_os_14_anos"
    

    try:
        service = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=service)
        
        navegador.get(urlPage)
        time.sleep(4)
        
        lista_dez_filmes = WebDriverWait(navegador, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="mw-content-text"]/div[1]/ul[1]/li')))
        lista_outros_filmes = WebDriverWait(navegador, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="mw-content-text"]/div[1]/div[1]/ul/li')))
        
        todos_filmes = []
        
        for filme in lista_dez_filmes:
            nome_filme, data_filme = filme.text.split(' (')
            todos_filmes.append({"Nome filme": nome_filme, "Data filme": data_filme.rstrip(')')})
        
        for filme in lista_outros_filmes:
            nome_filme, data_filme = filme.text.split(' (')
            todos_filmes.append({"Nome filme": nome_filme, "Data filme": data_filme.rstrip(')')})
        
        total = len(todos_filmes)
        todos_filmes.append({"Nome filme": 'Total de filmes', "Data filme": total})

        df_todos_filmes = pd.DataFrame(todos_filmes)
        
        df_todos_filmes.to_excel('filmes.xlsx', index=False)
        
        navegador.quit()
    except:
        print("Ocorreu um erro")

get_filmes()

