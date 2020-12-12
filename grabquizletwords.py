from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import win32clipboard
from login import Login
import time
PATH = "chromedriver_win32\chromedriver.exe"
#region OptionalMobileEmulation
# mobile_emulation = { "deviceName": "Nexus 5" }
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# driver = webdriver.Chrome(PATH,desired_capabilities = chrome_options.to_capabilities())
#endregion
def GrabWordsFromQuizlet(link,driver):
    driver.get(link)
    driver.execute_script("window.scrollTo(0,1000)") 
    while True:
        try:
            terms = driver.find_elements_by_xpath("//div[@id='SetPageTarget']//div[@class='SetPage-setContentWrapper']//div[@class='SetPage-setDetailsTermsWrapper']//div[2][@class='SetPage-content']//div[@class='SetPage-terms']//section[@class='SetPageTerms-termsList']//div[@class='SetPageTerms-term']")
            if(len(terms) > 0):
                break
        except Exception as e:
            print(e)
            pass
    WordList = ""
    for term in terms:
        term = term.text.split("\n")
        word = term[0]
        definition = term[1]
        WordList += word +"*(#"+definition + "@#$"
    WordList = WordList[:-3]
    print(WordList)
    return WordList
#GrabWordsFromQuizlet("https://quizlet.com/528642675/atom-and-nuclear-advanced-quizlet-flash-cards/",driver)