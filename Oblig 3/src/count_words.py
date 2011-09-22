import sys,re, getopt
usage = 'Usage: %s file word' % sys.argv[0]

try:
    options, args = getopt.getopt(sys.argv[1:], 'ib', ['insensetive', 'boundaries'])
    infilename = args[0]
    word = args[1]
except:
    print usage; sys.exit(1)
reg = 0; worder= word #default
for option, value in options:
    if option in ('-i', '--insensetive'):
        reg = re.I
    elif option in ('-b', '--boundaries'):
        worder = r"\b" + word + r"\b"

ifile = open(infilename, 'r').read() # opens file for reading, pushes to string
value = re.findall(worder, ifile, reg)
print 'The term \'%s\' occurred %d times' % (word, len(value))
       
