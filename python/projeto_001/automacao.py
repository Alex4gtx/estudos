from selenium import webdriver
from time import sleep

navegador = webdriver.Chrome()

url = 'https://keybase.io/warp/warp_1.0.9_SHA256_a2067491ab582bde779f4505055807c2479354633a2216b22cf1e92d1a6e4a87.html'

public_key = '1PqqJxvB8n983FEsF9pdCZCXHTM5Hi77Gr'
x = 'xpath'

navegador.get(url)

sleep(4)
navegador.find_element(x, '//*[@id="passphrase"]').click()
sleep(1)
navegador.find_element(x, '//*[@id="passphrase"]').send_keys('alex')
navegador.find_element(x, '//*[@id="btn-submit"]').click()
sleep(18.5)
navegador.find_element(x, '')