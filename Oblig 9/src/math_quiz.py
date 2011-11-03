import sys
from random import randint 

limits = [10,25,100]; gameOn=True

def result(q, n1, n2): #q is question type
    if (q == 1):
        return {'type':'plus', 'res':n1+n2}
    elif (q == 2):
        return  {'type':'minus', 'res':n1-n2}
    elif (q == 3):
        return  {'type':'times', 'res':n1*n2}
    else:
        return result(randint(1,3), n1, n2) #if mixed get random
    
while (gameOn == True): #makes it possible to restart the game
    questions = 0; correct = 0; #reset
    try:
        questions = int(input("How many questions? "))
        level = int(input("Skill level: 1=Beginner, 2=Intermediate, 3=Advanced : "))
        if (level < 1 or level > 3): raise Exception
        questionType = int(input("Should the questions be 1=Addition, 2=Subtraction, 3=Multiplication or 4=Mixed? "))
        if (level < 1 or level > 4): raise Exception 
       
    except:
        print ("Wrong input!")
        sys.exit(0)

    for i in range(questions):
        n1 = randint(1, limits[level-1]) # get number 1
        n2 = randint(1, limits[level-1]) # get number 2
        res = result(questionType, n1, n2) #returns result
        ans = input("What's %d %s %d? " % (n1, res['type'], n2))
        if ans == res['res']:
            print "That's right -- well done.\n"
            correct = correct + 1
        else:
            print "No, I'm afraid the answer is %d.\n" % res['res']
    
    print "\nI asked you %d questions.  You got %d of them right." % (questions, correct)
    percentage = float(correct)/float(questions)
    if (percentage > 0.67):
        print "Well Done!"
    elif (percentage > 0.33):
        print "You need more practice!"
    else:
        print "Please ask your math teacher for help!"
    
    cont = raw_input("Play again? (Y)es, (N)o : ")
    if (cont.lower() != 'y'): break # stops the game if Y is not pressed 
    
    """
> python math_quiz.py

How many questions? 2
Skill level: 1=Beginner, 2=Intermediate, 3=Advanced : 3
Should the questions be 1=Addition, 2=Subtraction, 3=Multiplication or 4=Mixed? 4
What's 55 times 41? 1304
No, I'm afraid the answer is 2255.

What's 83 times 43? 3569
That's right -- well done.


I asked you 2 questions.  You got 1 of them right.
You need more practice!
Play again? (Y)es, (N)o : Y

How many questions? 1
Skill level: 1=Beginner, 2=Intermediate, 3=Advanced : 1
Should the questions be 1=Addition, 2=Subtraction, 3=Multiplication or 4=Mixed? 2
What's 8 minus 5? 3
That's right -- well done.


I asked you 1 questions.  You got 1 of them right.
Well Done!
Play again? (Y)es, (N)o : z
"""