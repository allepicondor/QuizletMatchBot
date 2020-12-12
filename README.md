# QuizletMatchBot
For quizlet match games can get as low as .7 seconds works on 99% of quizlets
## Basic Start Guide:
	1. Clone this repository

	2. Install Pip modules.
		pip install selenium

	3. Find the quizlet code for your selected quizlet by looking at the url ex. quizlet.com/ **123456789** /NAMEOFQUIZLETSET/ -> **123456789**

	4. CD to directory og QuizletBot.py 

	5. Run command "py QuizletBot.py -GrabWords -KO QUIZLETCODE" in cmd
## Common Problems
	1. Loading the website version of Quizlet instead of the mobile verison.
		This is and easy fix add the argument -mobile or -m ex. "py QuizletBot.py -GrabWords **-m** -KO QUIZLETCODE" 
	2. Super long quizlets dont work.
		I know i'll fix later.
