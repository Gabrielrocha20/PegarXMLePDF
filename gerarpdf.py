
import os
from subprocess import CREATE_NO_WINDOW
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PegarPDF:
    def __init__(self):
        pass
    def baixarPDF(self, notas):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--headless=new")
        chrome_service = ChromeService("./chromedriver.exe")
        chrome_service.creationflags = CREATE_NO_WINDOW
        driver = webdriver.Chrome(service=chrome_service,options=options)
        driver.get("https://www.fsist.com.br/converter-xml-nfe-para-danfe")
        
        elem = driver.find_element(By.XPATH, '//*[@id="arquivo"]')
        for nota in notas:
            elem.send_keys(nota[0])

        send = driver.find_element(By.XPATH, '//*[@id="divPlaceHolder"]/div[1]/table[1]/tbody/tr[1]/td[2]/label')
        send.click()

        aceitar = driver.find_element(By.XPATH, '//*[@id="msgsim"]')
        aceitar.click()
        sleep(5)

        baixar = driver.find_element(By.XPATH, '//*[@id="butlinktexto"]')
        baixar.click()

        sleep(5)

        driver.close()
        driver.quit()

        return True

if __name__ == "__main__":
    a = PegarPDF()
    a.baixarPDF()