# QuizletMatchBot
 For quizlet match games can get as low as .7 seconds works on 99% of quizlets
 
1. Install Pip modules.
    pip install selenium
    
2. go to the quizlet you want to use and hit the More button (3 horizontal dots).
 
3. select export.
 
4. once in export menu for Between term and definition select CUSTOM and change the placeholder to "*(#".
 
5. For Between rows select Custom and change the placeholder to "@#$".

    [ExampleExport](https://raw.githubusercontent.com/allepicondor/QuizletMatchBot/main/images/Export.PNG)
    
6. Now hit Copy text and paste it in a file in the directory of main.py, after you paste it check to make sure there is no "@#$" as the last chars of the text if there is delete    it you can save it as "answers"
 
7. Open CMD and cd into the main.py directory ex"cd C://path/to/main.py" after you cd run the python file like this
     python SeleniumMain.py https://quizletlink/match answers
