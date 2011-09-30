import random, sys

try:
    n = eval(sys.argv[1])
except:
    print 'Missing n: Example -> dice2.py 10000'; sys.exit(0)
def Dice(): #Throws a dice
    return random.randint(1,6)

def compute(n):
    count = 0
    for n in range(1, n):
        if (Dice() == 6 or Dice() == 6): #if one of the dices are 6
            count += 1
    return count

print 'n=%d, p=%.3f' % (n, compute(n)/float(n))

"""
> python dice2.py 300000
n=300000, p=0.306
> python dice2.py 100
n=100, p=0.230
"""
