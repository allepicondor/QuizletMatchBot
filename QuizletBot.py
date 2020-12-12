from base64 import encode
from selenium import webdriver
from login import Login
from grabquizletwords import GrabWordsFromQuizlet
import time
import argparse
parser = argparse.ArgumentParser(description='Quizlet Bot')
parser.add_argument('QuizletCode', metavar='L', type=str, nargs='+',
                    help='Code to your quizlet can be found in url ex. 542807048 is the code for https://quizlet.com/542807048/ ')
parser.add_argument('-VocabList',type=str,
                    help='File path to the answer txt of yout quizlet')
parser.add_argument('-ROR', '--ROR',help="Run on repeat",action='store_true')
parser.add_argument('-KO', '--KO',help="Keep window open",action='store_false')
parser.add_argument('-GrabWords', '--GrabWords',help="Grab The vocab list for you REQUIRES LOGIN",action='store_true')
parser.add_argument('-SaveFile', '--SaveFile',help="save file after grab words",action='store_true')
parser.add_argument('-username', '--username',"-u",help="Optional leave blank if you dont want it to sign in.")
parser.add_argument('-password', '--password',"-p",help="Optional leave blank if you dont want it to sign in.")
parser.add_argument('-mobile', '--mobile',"-m",help="Optional only use of not getting mobile page and is instead getting the desktop version.",action='store_true')
args = parser.parse_args()
print(args.QuizletCode)

PATH = "chromedriver_win32\chromedriver.exe"
QUIZLETLINK = "https://quizlet.com/"+str(args.QuizletCode[0])
FILE_PATH = args.VocabList
RUN_ON_REPEAT = args.ROR
KEEPOPEN = args.KO
GrabWords=args.GrabWords
loggedIn=False
try:
    open("Sets/"+str(args.QuizletCode[0])+".txt", 'r', encoding='utf-8')
    if(input("You already have vocab list downloaded from previous run if you would rather use this one? (y/N)") == "y"):
        GrabWords = False
        FILE_PATH = "Sets/"+str(args.QuizletCode[0])+".txt"
except Exception:
    pass
if not GrabWords:
    file1 = open(FILE_PATH, 'r', encoding='utf-8')
    file1 = file1.read().split("@#$")
if(args.mobile):
    mobile_emulation = { "deviceName": "Nexus 5" }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(PATH,desired_capabilities = chrome_options.to_capabilities())
else:
    driver = webdriver.Chrome(PATH)
if(GrabWords):
    file1 = GrabWordsFromQuizlet(QUIZLETLINK,driver)
    if(args.SaveFile):
        file3 = open("Sets/"+str(args.QuizletCode[0])+".txt","w",encoding='utf-8') 
    file1 = file1.split("@#$")
if not (args.username == None and args.password == None):
    Login(args.username,args.password,driver)
    loggedIn=True
    time.sleep(1)
badChars = ["/","(",")","[","]"]
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',' ']
def textCleanUp(text):
    text = text.replace("\n"," ")
    text = text.replace("\r"," ")
    text = text.replace(" ", "")

    return text
Terms = []
Definitions=[]
termToDefinitions = {}
for word in file1:
   word = word.split("*(#")
   term = textCleanUp(word[0])
   definition = textCleanUp(word[1])
   Terms.append(term)
   Definitions.append(definition)
   termToDefinitions[term] = definition
while True:
    driver.get(QUIZLETLINK+"/match")
    StartButton = driver.find_element_by_class_name("UIButton.UIButton--hero" )
    StartButton.click()
    tiles = driver.find_elements_by_class_name("MatchModeQuestionGridBoard-tile")
    TermTiles = {}
    DefinitionTiles = {}

    for tile in tiles:
        while tile.text == "":
            pass
        text = textCleanUp(tile.text)
        if text in Terms:
            TermTiles[text] = tile
        elif text in Definitions:
            DefinitionTiles[text] = tile
        else:
            print(text,":",definition)
            print("_____________")
            print("Terms READ IN",Terms)
            print("_____________")
            print("Definitions READ IN",Definitions)
            raise TypeError
    #print("_________")
    #print(DefinitionTiles.keys())
    for Term in TermTiles.keys():
        ads = termToDefinitions[Term]
        answerTile = DefinitionTiles[ads]
        tile = TermTiles[Term]
        if(answerTile != None):
            tile.click()
            answerTile.click()
    if(RUN_ON_REPEAT):
        continue
    else:
        break
if(KEEPOPEN):
    while(True):
        pass
