import random, sys

try:
    n = eval(sys.argv[1])
except:
    print 'Missing n: Example -> dice4.py 10000'; sys.exit(0)
def Dice():
    return random.randint(1,6)

def compute(n):
    pot = 0
    for n in range(1, n):
        pot -= 1 # removes one unit to play the game
        if ( (Dice() + Dice() + Dice() + Dice()) < 9):
            pot += 10 # updates the pot if sum is < 9
    return pot

computed = compute(n)
if (computed > 0):
    print 'You should play this game. Sum after %d games: %d units' % (n, computed)
else:
    print 'You should not play this game. Sum after %d games: %d units' % (n, computed)

"""
> python dice4.py 10000
You should not play this game. Sum after 10000 games: -4739 units
"""
