import os
import time
import sys
from selenium import webdriver
from extractSentence import checkExercices
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def logIn():
    sys.setrecursionlimit(10000)
    driver_path = 'chromedriver-win64/chromedriver.exe'

    service = Service(driver_path)

    driver = webdriver.Chrome(service=service)

    driver.get(
        "https://www.projet-voltaire.fr/voltaire/com.woonoz.gwt.woonoz.Voltaire/Voltaire.html?returnUrl=www.projet"
        "-voltaire.fr/choix-parcours/&applicationCode=pv")

    usernameBox = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'user_pseudonym'))
    )
    passwordBox = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'user_password'))
    )

    with open('login.txt', 'r') as file:
        mail = file.readline().strip()
        password = file.readline().strip()

    usernameBox.send_keys(mail)
    passwordBox.send_keys(password)

    loginButton = driver.find_element(By.ID, 'login-btn')
    loginButton.click()

    os.system('cls')

    time.sleep(8)
    checkExercices(driver)
