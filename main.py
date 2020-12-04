from PIL import ImageGrab
import pytesseract
import mouse
import time
from tkinter import *
# Using readlines() 
file1 = open('EnglishUnit3.txt', 'r') 
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
    bestKey = None
    currentBest = 0
    for key in wordlist:
        total = 0
        index = 0
        for letter in key:
            if(text.count(letter) > 0):
                total+=1
            if index < len(text)-1 and letter == text[index]:
                total+= 10
            index+=1
        if total > currentBest:
            currentBest = total
            bestKey = key
    return bestKey
def stop():
    print("stoping")
    loc = root.geometry()
    loc = loc.split("+")
    WinSize = loc[0]
    loc = [int(loc[1])+5,int(loc[2])+30]
    WinSize = WinSize.split("x")
    WinSize = [int(WinSize[0]),int(WinSize[1])]
    root.destroy()
    mouse.move(1186,423, absolute=True, duration=0.001)
    mouse.click('left')
    time.sleep(0.75)
    image = ImageGrab.grab(bbox=(loc[0],loc[1],loc[0]+WinSize[0],loc[1] + WinSize[1]))
    image.save("sc.png")
    ImageArray = [[None,None,None,None],[None,None,None,None],[None,None,None,None]]
    TextArray = [[None,None,None,None],[None,None,None,None],[None,None,None,None]]
    HitArray = {}
    for x in range(3):
        for y in range(4):
            location = [int(x*(WinSize[0]/3)),int(y*(WinSize[1]/4)),int(x*(WinSize[0]/3)) +int((WinSize[0]/3)),int(y*(WinSize[1]/4))+int((WinSize[1]/4))]
            ImageArray[x][y] = image.crop(location)
            text = pytesseract.image_to_string(ImageArray[x][y])
            text = textCleanUp(text)
            TextArray[x][y] = text
            HitArray[text] = [loc[0]+ int(x*(WinSize[0]/3))+((WinSize[0]/3)/2),loc[1]+int(y*(WinSize[1]/4))+((WinSize[1]/4)/2)]
    pairing = []
    answerstoword = []
    for word in HitArray.keys():
        print(word)
        try:
            answer = answers[word]
        except KeyError as e:
            continue
        keyWord = FindSimilarWords(answer,HitArray.keys())
        answerstoword.append([word,answer])
        pairing.append([HitArray[word],HitArray[keyWord]])
    print("answers: ",answers.keys())
    print("answerstowords: ",answerstoword)
    for pair in pairing:
        AnswerFromTwoPos(pair[0],pair[1])
for line in Lines: 
    line = line.split(":")
    word = textCleanUp(line[0])
    definition = textCleanUp(line[1])
    answers[word] = definition
root = Tk()
B = Button(root, text ="Start", command = stop)
root.geometry("400x400")
root.attributes('-alpha',0.3)
B.pack()
root.mainloop()
