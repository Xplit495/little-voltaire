import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def login(driver: webdriver.Chrome):

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

    print("You have 15 seconds to choose the level on which you want the bot to spend time.")
    time.sleep(15)
    return
