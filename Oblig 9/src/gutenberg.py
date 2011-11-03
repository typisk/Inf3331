def count(infile):
    import sys, re
    try:
        f = open(infile, 'r').read();
    except:
        print "No file found."
        sys.exit(0)
    all = {} # collector
    r = re.compile(r'\w+') # only words or numbers
    for matchg in r.finditer(f): #for all matches
        match = matchg.group()
        if match in all: #check if exists
            all[match] += 1 #just doing this without if-else crashes
        else:
            all[match] = 1
    sorted = all.items()
    sorted.sort()
    return sorted

result = count('fotball.txt') #from earlier exercise
for i in result:
    print "%s: %d" % (i[0], i[1])
    
"""
11: 1
90: 1
After: 1
Football: 1
...
two: 2
use: 2
win: 1
"""