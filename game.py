import random

l = ["rock", "scissor", "paper"]
while True:
    ccount = 0
    ucount = 0
    DrawMatch = 0
    uc = int(input('''
    Game Start.....
    1 Yes
    2 No | Exit

         '''))

    if uc == 1:
        for a in range(0, 5):
            userinput = int(input('''

    1 Rock 
    2 Scissor 
    3 Paper 

            '''))

            if userinput == 1:
                uchoice = "rock"
            elif userinput == 2:
                uchoice = "scissor"
            elif userinput == 3:
                uchoice = "paper"

            Cchoice = random.choice(l)
            if Cchoice == uchoice:
                print("computer value",Cchoice)
                print("user value",uchoice)
                print("game Draw")
                DrawMatch = DrawMatch +1
                # ucount = ucount +1
                # ccount = ccount +1
            elif(uchoice=='rock' and Cchoice=="scissor") or (uchoice==
                'scissor' and Cchoice=="paper") or (uchoice == "paper"
                and Cchoice=="rock"):
                print("computer value", Cchoice)
                print("user value", uchoice)
                print("user is ♂️🧛🧚🏻Winner")
                ucount = ucount +1;
            else:
                print("computer value", Cchoice)
                print("user value", uchoice)
                print("computer is ♂️🧛🧚🏻Winner")
                ccount = ccount +1

        print("your final Result:-----")
        print("..........")
        print("..........")
        print("..........")
        if ucount>ccount:
          print("you is winner🤪🤪🤪 by"+str(ucount)+"vs"+str(ccount))
          print("because "+str(DrawMatch)+" drawMatch")
        else:
          print("computer is winner🤪🤪🤪 by"+str(ccount)+"vs"+str(ucount))
          print("because "+str(DrawMatch)+" drawMatch")
    else:
       break
