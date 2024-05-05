import time
import random
from logIn import logIn
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def checkExercises(driver: webdriver.Chrome):
    time.sleep(1)
    logIn(driver)
    while True:
        time.sleep(5)
        try:
            driver.find_element(By.CLASS_NAME, 'understoodButton').click()
            time.sleep(2)

            popupButton = driver.find_element(By.CLASS_NAME, 'popupButton')
            if popupButton.is_displayed() and popupButton.is_enabled():
                popupButton.click()

            driver.find_element(By.CLASS_NAME, 'intensiveLessonVideoTitle')
            driver.find_element(By.CLASS_NAME, 'understoodButton').click()
            handleRandomButtons(driver)

            handleSpecialCase(driver)

        except NoSuchElementException:
            randomClick(driver, extractSentence(driver))
            time.sleep(1)
            driver.find_element(By.CLASS_NAME, 'nextButton').click()


def handleSpecialCase(driver: webdriver.Chrome):
    try:
        specialElement = driver.find_element(By.CLASS_NAME, 'gwt-InlineHTML')
        if specialElement.is_enabled() and specialElement.is_displayed():
            driver.find_element(By.CLASS_NAME, 'validateButton').click()
            driver.find_element(By.CLASS_NAME, 'nextButton').click()
            checkExercises(driver)
    except NoSuchElementException:
        sentenceArray = extractSentence(driver)
        randomClick(driver, sentenceArray)


def extractSentence(driver: webdriver.Chrome):
    time.sleep(1)
    elements = driver.find_elements(By.CLASS_NAME, "pointAndClickSpan")

    return [element.text for element in elements if element.text != "'"]


def handleRandomButtons(driver: webdriver.Chrome):
    buttonOk = driver.find_elements(By.CLASS_NAME, 'buttonOk')
    buttonKo = driver.find_elements(By.CLASS_NAME, 'buttonKo')

    for i in range(3):
        time.sleep(2)
        randomChoice = random.choice([0, 1])
        if randomChoice == 0 and i < len(buttonOk):
            buttonOk[i].click()
        elif i < len(buttonKo):
            buttonKo[i].click()
    return


def randomClick(driver: webdriver.Chrome, sentence):

    elementToClick = random.randint(0, len(sentence))

    if elementToClick == len(sentence):
        nextQuestionButtons = driver.find_elements(By.CLASS_NAME, 'noMistakeButton')
        for button in nextQuestionButtons:
            if button.is_displayed() and button.is_enabled():
                button.click()
    else:
        wordToClick = sentence[elementToClick]
        xpath = f"//span[@class='pointAndClickSpan' and contains(text(), '{wordToClick}')]"
        italicXpath = f"//span[@class='pointAndClickSpan italic' and contains(text(), '{wordToClick}')]"
        try:
            driver.find_element(By.XPATH, xpath).click()
        except NoSuchElementException:
            driver.find_element(By.XPATH, italicXpath).click()
    return
