from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

options = webdriver.ChromeOptions()

options.add_argument("--headless")

navegador = webdriver.Chrome(chrome_options=options)

navegador.get("https://asesweb.governoeletronico.gov.br")

urls = ['www.tjro.jus.br/', 'https://www.tjro.jus.br/resp-institucional/resp-conheca-pj',
        'https://www.tjro.jus.br/resp-institucional/resp-conheca-pj']
for url in urls:

    navegador.find_element(By.ID, 'url').send_keys(url)
    navegador.find_element(By.XPATH, '//*[@id="input_tab_1"]').click()
    # time.sleep(10)

    rows = len(navegador.find_elements(By.XPATH, '/html/body/section/div/div[1]/div[4]/div[2]/div[3]/table/tbody/tr'))
    cols = len(navegador.find_elements(By.XPATH, '/html/body/section/div/div[1]/div[4]/div[2]/div[3]/table/tbody/tr[1]/td'))

    row_total = len(navegador.find_elements(By.XPATH,'/html/body/section/div/div[1]/div[4]/div[2]/div[3]/table/tfoot/tr/td'))
    percentage = len(navegador.find_elements((By.XPATH,'/html/body/section/div/div[1]/div[4]/div[2]/div[1]/div/div/span')))


    result = []
    for i in range(1, rows + 1):
        d = []
        for j in range(1, cols + 1):
            d.append(navegador.find_element(By.XPATH,"//*[@id='tabelaErros']/tbody/tr[" + str(i) + "]/td[" + str(j) + "]").text)
        result.append({"secao": d[0], "erros": d[1], "avisos": d[2]})

    print(result)

    # with open('ases_data.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerows()
