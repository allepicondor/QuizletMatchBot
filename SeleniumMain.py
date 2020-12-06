from selenium import webdriver
PATH = "chromedriver_win32\chromedriver.exe"
QUIZLETLINK = "https://quizlet.com/XXXXXXXX/match"
FILE_PATH = "PolyatomicIons"
RUN_ON_REPEAT = True
KEEPOPEN = False
driver = webdriver.Chrome(PATH)

badChars = ["/","(",")","[","]"]
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',' ']
def textCleanUp(text):
    return text.strip()
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
file1 = open(FILE_PATH, 'r', encoding='utf-8')
file1 = file1.read().split("@#$")
Terms = []
Definitions=[]
termToDefinitions = {}
for word in file1:
   word = word.split("*(#")
   term = word[0]
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
