from PIL import ImageGrab
import pytesseract
import mouse
import keyboard
import time
from tkinter import *
#SETTINGS
waitTime = 0.7
thershold = 70
file1 = open('EnglishUnit3.txt', 'r') 
ShowTimes = True
DebugMode = False
#SETTINGS


root = Tk()
selectedPos = []

Lines = file1.readlines() 
answers = {}
count = 0
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
loc = []
WinSize = 0
badChars = ["/","(",")","[","]"]
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',' ']
def textCleanUp(text):
    text = text.replace("Syn","_")
    text = text.replace("Ant","_")
    text = text.replace("SYNONYMS","_")
    text = text.replace("ANTONYMS","_")
    text = text.lower()
    text = text.replace(","," ")
    text = text.replace(";"," ")

    newString = ""
    removeingMode = False
    for letter in text:
        if (letter in alphabet) and not removeingMode:
            newString += letter
        elif (letter == "[" or letter == "("):
            removeingMode = True
        elif(letter == "]" or letter == ")" and removeingMode):
            removeingMode = False
        elif letter == "_":
            break
    return newString.replace(" ","")
def AnswerFromTwoPos(pos1,pos2):
    mouse.move(pos1[0], pos1[1], absolute=True, duration=0.0001)
    mouse.click('left')
    mouse.move(pos2[0], pos2[1], absolute=True, duration=0.0001)
    mouse.click('left')
def FindSimilarWords(text,wordlist):
    def BigBoiMath(score):
        return (11*score)- 10
    text = text.strip()
    bestKey = None
    currentBest = 0
    for key in wordlist:
        key = key.strip()
        total = -abs(len(key) - len(text))
        index = 0
        for letter in key:
            if(text.count(letter) > 0):
                total+=1
            if index < len(text)-1 and letter == text[index]:
                total+=10
            index+=1
        total*= (100/BigBoiMath(len(text)))
        if total > currentBest:
            currentBest = total
            bestKey = key
    return bestKey,currentBest
def StartBot():
    print("Bot Ready Hit Enter to start")
    loc = root.geometry()
    loc = loc.split("+")
    WinSize = loc[0]
    loc = [int(loc[1])+5,int(loc[2])+30]
    #loc = [int(loc[1]*2),int(loc[2]*2)+30]
    WinSize = WinSize.split("x")
    #WinSize = [int(WinSize[0])*2,int(WinSize[1])*2]
    WinSize = [int(WinSize[0]),int(WinSize[1])]
    root.withdraw()
    while True:
        if (keyboard.is_pressed("enter")):
            break
    if(DebugMode or ShowTimes):
        tic = time.perf_counter()
    #mouse.move(selectedPos[0], selectedPos[1], absolute=True, duration=0)
    #mouse.click('left')
    print("Waiting for page load")
    time.sleep(waitTime)
    print("Starting Bot")
    image = ImageGrab.grab(bbox=(loc[0],loc[1],loc[0]+WinSize[0],loc[1] + WinSize[1]))
    HitArray = {}
    if(DebugMode):
        image.save("OutputImages/"+"Output.png")
    if(DebugMode or ShowTimes):
        toc = time.perf_counter()
        print(f"Setup in  {toc - tic:0.4f} seconds")
        tic = time.perf_counter()
    for x in range(3):
        for y in range(4):
            location = [int(x*(WinSize[0]/3)),int(y*(WinSize[1]/4)),int(x*(WinSize[0]/3)) +int((WinSize[0]/3)),int(y*(WinSize[1]/4))+int((WinSize[1]/4))]
            NewImage = image.crop(location)
            text = pytesseract.image_to_string(NewImage)
            text = textCleanUp(text)
            if(DebugMode):
                NewImage.save("OutputImages/"+str([x,y])+".png")
            HitArray[text] = [loc[0]+ int(x*(WinSize[0]/3))+((WinSize[0]/3)/2),loc[1]+int(y*(WinSize[1]/4))+((WinSize[1]/4)/2)]
    if(DebugMode  or ShowTimes):
        toc = time.perf_counter()
        print(f"Went through all images in  {toc - tic:0.4f} seconds")
    pairing = []
    answerstoword = []
    if(DebugMode):
        print("_____________")
        print(HitArray.keys())
    if(DebugMode or ShowTimes):
        tic = time.perf_counter()
    for word in HitArray.keys():
        try:
            keyWordA,score = FindSimilarWords(word,answers.keys())
            if(DebugMode):
                print("word:",word,"FoundWordSimilar",keyWordA,"with score of ",score,"PASS:",score < 50)
            if(score < thershold):
                raise KeyError
            answer = answers[keyWordA]
        except KeyError as e:
            continue
        keyWord,score = FindSimilarWords(answer,HitArray.keys())
        answerstoword.append([word,answer])
        pairing.append([HitArray[word],HitArray[keyWord]])
    if(ShowTimes or DebugMode):
        toc = time.perf_counter()
        print(f"Generated mouse movements in {toc - tic:0.4f} seconds")
    if(DebugMode):
        print(answerstoword)
        print("TOTAL: "+str(len(pairing))+"/6")
        print("answers: ",answers.keys())
        print("answerstowords: ",answerstoword)
    if(DebugMode or ShowTimes):
        tic = time.perf_counter()
    for pair in pairing:
        AnswerFromTwoPos(pair[0],pair[1])
    if(DebugMode or ShowTimes):
        toc = time.perf_counter()
        print(f"Moved Mouse in {toc - tic:0.4f} seconds")
    root.deiconify()
def Setup():

    for line in Lines: 
        line = line.split(":")
        word = textCleanUp(line[0])
        definition = textCleanUp(line[1])
        answers[word] = definition
    B = Button(root, text ="Start", command = StartBot)
    root.geometry("400x400")
    root.attributes('-alpha',0.3)
    B.pack()
    print("resize window && select start pos")
    while True:
        if (keyboard.is_pressed("s")):
            selectedPos = mouse.get_position()
            if(DebugMode):
                print("Start Button Updated", selectedPos)
        root.update_idletasks()
        root.update()
Setup()
