import sys, random

n = sys.argv[1] # times to run
l = []
for i in range( int(n) ):
    l.append( random.uniform(-1,1) )
else:
    average = float( sum(l) /  len(l))
print 'Gjennomsnittet ble: %.4f' % average
    

    
    


