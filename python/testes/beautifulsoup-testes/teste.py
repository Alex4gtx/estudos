from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='chromedriver.exe')

url = r'https://keybase.io/warp/warp_1.0.9_SHA256_a2067491ab582bde779f4505055807c2479354633a2216b22cf1e92d1a6e4a87.html'

driver.get(url)
sleep(3)

driver.find_element_by_xpath('//*[@id="passphrase"]//div')
