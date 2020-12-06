from selenium import webdriver
import argparse
parser = argparse.ArgumentParser(description='Quizlet Bot')
parser.add_argument('QuizletMatchLink', metavar='L', type=str, nargs='+',
                    help='Link to your quizlet match game')
parser.add_argument('AnswersLocalFilePath', metavar='F', type=str, nargs='+',
                    help='File path to the answer txt of yout quizlet')
parser.add_argument('-ROR', '--ROR',help="Run on repeat",action='store_true')
parser.add_argument('-KO', '--KO',help="Keep window open",action='store_true')
args = parser.parse_args()
print(args.QuizletMatchLink)


PATH = "chromedriver_win32\chromedriver.exe"
QUIZLETLINK = args.QuizletMatchLink[0]
FILE_PATH = args.AnswersLocalFilePath[0]
RUN_ON_REPEAT = args.ROR
KEEPOPEN = args.KO
if(not "/match" in QUIZLETLINK):
    print("INVALID LINK: use a match link like https://quizlet.com/551580491/match. You can get it by clicking on MATCH on the quizlet then copying the link.")
    raise TypeError
file1 = open(FILE_PATH, 'r', encoding='utf-8')

driver = webdriver.Chrome(PATH)

badChars = ["/","(",")","[","]"]
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',' ']
def textCleanUp(text):
    text = text.replace("\n"," ")
    text = text.replace(" ", "")

    return text
    # text = text.replace("Syn","_")
    # text = text.replace("Ant","_")
    # text = text.replace("SYNONYMS","_")
    # text = text.replace("ANTONYMS","_")
    # text = text.replace("\n"," ")
    # text = text.lower()
    # text = text.replace(","," ")
    # text = text.replace(";"," ")

    # newString = ""
    # removeingMode = False
    # for letter in text:
    #     if (letter in alphabet) and not removeingMode:
    #         newString += letter
    #     elif (letter == "[" or letter == "("):
    #         removeingMode = True
    #     elif(letter == "]" or letter == ")" and removeingMode):
    #         removeingMode = False
    #     elif letter == "_":
    #         break
    # return newString.replace(" ","")
file1 = file1.read().split("@#$")
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
    driver.get(QUIZLETLINK)
    StartButton = driver.find_element_by_class_name("UIButton.UIButton--hero" )
    StartButton.click()
    tiles = driver.find_elements_by_class_name("MatchModeQuestionGridBoard-tile")
    TermTiles = {}
    DefinitionTiles = {}

    for tile in tiles:
        while tile.text == "":
            pass
        text = tile.text
        definition = textCleanUp(text)
        if text in Terms:
            TermTiles[text] = tile
        elif definition in Definitions:
            DefinitionTiles[definition] = tile
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
