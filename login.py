from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
PATH = "chromedriver_win32\chromedriver.exe"
def Login(USERNAME,PASSWORD,driver):
    driver.get("https://quizlet.com/login")
    while True:
        try:
            usernamefield = driver.find_element_by_id("username")
            passwordfield = driver.find_element_by_id("password")
            break
        except Exception as e:
            pass
    submitButton = driver.find_element_by_xpath('//button[@aria-label="Log in"]')
    usernamefield.send_keys(USERNAME)
    passwordfield.send_keys(PASSWORD)
    submitButton.click()
