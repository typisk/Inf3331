class Roshambo:            
    def __init__(self):
        print "Welcome to Rock, Paper, Scissors!\n"
        self.playerPoints = 0; self.computerPoints = 0
        
        win = int(input("How many points are required for a win?: "))
        
        while (self.playerPoints < win and self.computerPoints < win): #runs until win-score is reached
            pick = raw_input("Choose (R)ock, (P)aper, or (S)cissors?: ")
            self.calcWinner(pick.upper()) #Upper input so simplify
        
        print "Final Score: Human %d\t Computer %d" % (self.playerPoints, self.computerPoints)
    
    def calcWinner(self,player):
        import random
        valid = "RPS"; info = ["rock", "paper", "scissor"] 
        rand = random.randint(0,2)
        comp = valid[rand] #Picks character from valid
        
        if (player == comp):
            status = "A draw"
        elif ((player == "R" and comp == "S") or (player == "P" and comp == "R") or 
              (player == "S" and comp == "P")):
            status = "Human Wins!"
            self.playerPoints += 1
        else:
            status = "Computer Wins!"
            self.computerPoints += 1
        
        print "Human: %s\tComputer: %s\t\t%s\n" % (info[valid.index(player)], info[valid.index(comp)], status)
        
    
v = Roshambo()
"""
python roshambo.py
Welcome to Rock, Paper, Scissors!

How many points are required for a win?: 3
Choose (R)ock, (P)aper, or (S)cissors?: R
Human: rock    Computer: paper        Computer Wins!

Choose (R)ock, (P)aper, or (S)cissors?: R
Human: rock    Computer: rock        A draw

Choose (R)ock, (P)aper, or (S)cissors?: R
Human: rock    Computer: scissor        Human Wins!

Choose (R)ock, (P)aper, or (S)cissors?: P
Human: paper    Computer: rock        Human Wins!

Choose (R)ock, (P)aper, or (S)cissors?: S
Human: scissor    Computer: rock        Computer Wins!

Choose (R)ock, (P)aper, or (S)cissors?: R
Human: rock    Computer: scissor        Human Wins!

Final Score: Human 3     Computer 2
"""