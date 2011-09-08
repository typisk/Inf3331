import sys, os, time

usage = 'Usage: %s infile' % sys.argv[0]

try:
    infile = sys.argv[1]
except:
    print usage; sys.exit(1)
filename = os.path.splitext(infile)
suffix = time.strftime("_%b%d_%Y") #ex: Sep06_2011
os.rename(infile, filename[0] + suffix + filename[1])