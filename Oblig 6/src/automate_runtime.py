import sys,re, getopt, commands
usage = 'Usage: %s inputfile outputfile var1 var2 varN...' % sys.argv[0]

try:
    infile = sys.argv[1]; outfile = sys.argv[2]; args = sys.argv[3:]
except:
    print usage; sys.exit(1)

data = ''
cmd = 'python %s %s' % (infile, " ".join(args))

testfile = open(infile, 'r')
for line in testfile:
    data += line + '\n'

data += '\n\n"""\n'         # start rundtime example
data += 'Runtime example:\n'
data += cmd + '\n'          # example: python bar.py 2 3

failure, output = commands.getstatusoutput(cmd)
if failure:
    data += 'ERROR: Could not run\n', cmd; sys.exit(1)

for line in output.splitlines():
    data += line + '\n'

data += '"""' # end runtime example

outfile = open(outfile, 'w')
outfile.write(data)

"""
> python automate_runtime.py bar.py assignment.txt 2 3
> more assignment.txt 
#!/usr/bin/env python

def foo(arg1, arg2):
    return int(arg1) + int(arg2)

if __name__ == "__main__":
   import sys
   print foo(sys.argv[1], sys.argv[2])

\"""
Runtime example:
python bar.py 2 3
5
\"""

"""