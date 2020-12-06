from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import win32clipboard
from login import Login
import time
def GrabWordsFromQuizlet(link,driver):
    driver.get(link)
    time.sleep(2)
    action = ActionChains(driver)
    print("HERE")
    try:
        popup = driver.find_element_by_class_name("UIModalBody.is-fullWidth")
        close = driver.find_element_by_class_name("UIModal-closeButton")
        close.click()
    except Exception as e:
        print(e)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,1000)") 
    time.sleep(0.2)
    print("Finding EXPORT")
    moreButton = driver.find_element_by_xpath("//div[@id='SetPageTarget']//div[@class='SetPage-setDetails']//div[@aria-label='Options']//button[@title='More']")#/div/section/div/div/div
    action = ActionChains(driver)
    action.move_to_element(moreButton).click().perform()
    exportButton = driver.find_element_by_xpath("//*[@class='SetPage-menuPopover']//span[4]")
    print(exportButton)
    exportButton.click()
    time.sleep(1)
    print("EXPORT")
    textBox1 = driver.find_element_by_xpath("//input[@id='SetPageExportModal-CustomWordDelim-input']")
    textBox1.send_keys(Keys.CONTROL, 'a')
    textBox1.send_keys(Keys.BACKSPACE)
    textBox1.send_keys("*(#")
    textBox2= driver.find_element_by_xpath("//input[@id='SetPageExportModal-CustomRowDelim-input']")
    textBox2.send_keys(Keys.CONTROL, 'a')
    textBox2.send_keys(Keys.BACKSPACE)
    textBox2.send_keys("@#$")
    button = driver.find_element_by_xpath('//div[@class="UIModal UIModal-container is-white is-open"]//div[@class="SetPageExportModal-copyBtnWrapper"]/button')
    print(button)
    button.click()
    time.sleep(.5)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data
