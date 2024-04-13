import time
import random
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def checkExercices(driver: webdriver.Chrome):
    try:
        driver.find_element(By.CLASS_NAME, 'understoodButton').click()
        time.sleep(5)
        checkExercices(driver)
    except NoSuchElementException:
        ...
    try:
        element = driver.find_element(By.CLASS_NAME, 'popupButton')
        if element.is_displayed() and element.is_enabled():
            element.click()
    except NoSuchElementException:
        ...
    try:
        driver.find_element(By.CLASS_NAME, 'intensiveLessonVideoTitle')
        passPopUp(driver)
    except NoSuchElementException:
        isSpecial = False

        try:
            elt = driver.find_element(By.CLASS_NAME, 'gwt-InlineHTML')
            if elt.is_enabled() and elt.is_displayed():
                isSpecial = True
        except NoSuchElementException:
            ...

        if isSpecial:
            print("pipi")
            driver.find_element(By.CLASS_NAME, 'validateButton').click()
            time.sleep(2)
            driver.find_element(By.CLASS_NAME, 'nextButton').click()
            checkExercices(driver)
        else:
            sentenceArray = extractSentence(driver)
            elementToClick = random.randint(0, len(sentenceArray))
            randomClick(driver, sentenceArray, elementToClick)


def extractSentence(driver: webdriver.Chrome):
    time.sleep(3)
    elements = driver.find_elements(By.CLASS_NAME, 'pointAndClickSpan')

    sentenceArray = []

    for element in elements:
        if element.text == "'":
            ...
        else:
            sentenceArray.append(element.text)

    return sentenceArray


def passPopUp(driver: webdriver.Chrome):
    time.sleep(3)

    driver.find_element(By.CLASS_NAME, 'understoodButton').click()

    time.sleep(2)

    buttonOk = driver.find_elements(By.CLASS_NAME, 'buttonOk')
    buttonKo = driver.find_elements(By.CLASS_NAME, 'buttonKo')

    for i in range(3):
        time.sleep(3)
        randomChoose = random.randint(0, 1)
        if randomChoose == 0:
            buttonOk[i].click()
        else:
            buttonKo[i].click()

    time.sleep(2)

    try:
        driver.find_element(By.CLASS_NAME, 'exitButton').click()
        time.sleep(2)
        checkExercices(driver)
    except NoSuchElementException:
        element = driver.find_element(By.CLASS_NAME, 'showClueButton')
        if element.is_displayed() and element.is_enabled():
            checkExercices(driver)
        else:
            driver.find_element(By.CLASS_NAME, 'exitButton').click()
            time.sleep(2)
            checkExercices(driver)


def randomClick(driver: webdriver.Chrome, sentenceArray, elementToClick):
    time.sleep(6)

    if elementToClick == len(sentenceArray):
        nextQuestionButton = driver.find_elements(By.CLASS_NAME, 'noMistakeButton')
        time.sleep(2)
        for element in nextQuestionButton:
            if element.is_displayed() and element.is_enabled():
                element.click()
        time.sleep(2)
    else:
        wordToClick = sentenceArray[elementToClick]
        xpath = "//span[@class='pointAndClickSpan' and contains(text(), '" + str(wordToClick) + "')]"

        print("Mot :" + str(wordToClick))
        print("\nIndex :" + str(elementToClick) + "\nTableau :")
        print(sentenceArray)
        print("Xpath :" + xpath)

        time.sleep(2)

        try:
            driver.find_element(By.XPATH, xpath).click()
        except NoSuchElementException:
            print("Element not found, continue")
            time.sleep(2)
            checkExercices(driver)

        time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'nextButton').click()

    time.sleep(2)

    checkExercices(driver)
