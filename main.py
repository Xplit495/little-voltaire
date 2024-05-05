from extractSentence import checkExercises
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = 'chromedriver-win64/chromedriver.exe'

service = Service(driver_path)

driver = webdriver.Chrome(service=service)

driver.get(
    "https://www.projet-voltaire.fr/voltaire/com.woonoz.gwt.woonoz.Voltaire/Voltaire.html?returnUrl=www.projet"
    "-voltaire.fr/choix-parcours/&applicationCode=pv")

checkExercises(driver)
