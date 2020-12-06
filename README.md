# QuizletMatchBot
 For quizlet match games can get as low as .7 seconds works on 99% of quizlets
 
 1. Install Pip modules
    pip install selenium
 2. go to the quizlet you want to use and hit the More button (3 horizontal dots) and select export, 
 3. once in export menu for Between term and definition select CUSTOM and change the placeholder to "*(#", For Between rows select Custom and change the placeholder to "@#$"
    [ExampleExport](https://raw.githubusercontent.com/allepicondor/QuizletMatchBot/main/images/Export.PNG)
 4.Now hit Copy text and paste it in a file in the directory of main.py, after you paste it check to make sure there is no "@#$" as the last chars of the text if there is delete it
 5. go to main.py and change FILE_PATH to the name of the text file
 
 6. Open up main.py and change QUIZLETLINK to the match game link example link is "https://quizlet.com/XXXXXXXXX/match"
 
 7.run main.py in the directory of it
