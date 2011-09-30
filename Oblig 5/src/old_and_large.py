import os, time, getopt, sys, tempfile, shutil

try:
    options, args = getopt.getopt(sys.argv[1:], 'p:m:a:r',
                    ['path=', 'maxfilesize=', 'maxaccesstime=', 'delete'])
except:
    print 'Example: -p \'/home/vegard/workspace/Oblig 5/src/temp\' -m 12.0 -a 10 -r'
    print '-m is in megabytes'
    print '-a is in days'
    print '-r deletes the files'
    sys.exit(1)
    

remove = False; path = ''; maxf = 5.0; maxa = 14        #default values
temp = os.path.join(tempfile.gettempdir(), 'trash')     #so it works in Windows too!

for option, value in options:
    if option in ('-p', '--path'):
        path = value
    elif option in ('-m', '--maxfilesize'):
        maxf = eval(value)  #makes variable float
    elif option in ('-a', '--maxaccesstime'):
        maxa = eval(value)  #makes variable int
    elif option in ('-r', '--remove'):
        remove = True;


def checkFile(fil, maxfilesize, maxaccessed):
    if (os.path.getsize(fil) <= maxfilesize*1048576.0): #if less than xx.yy megabytes
        if (os.path.getatime(fil) >= time.time()-maxaccessed*24*3600): #accessed last X days
            return True
  

for direct, dirname, filename in os.walk(path):     #os.path.walk is deprecated
    for f in filename:
        theFile = os.path.join(direct,f)            #joins the filepath and file
        if(checkFile(theFile, maxf, maxa) == True):
            if (remove):                            #moves the file to temp if true
                if not os.path.exists(temp):        #check if temp exists
                    os.mkdir(temp)                  # if not, create it
                shutil.copy(theFile, os.path.join(temp,f))  #moves the file
                os.remove(theFile)                          #deletes the old file
                print 'Moved file %s to %s' % (theFile, temp)
            else:
                print f     #if no delete option, print file path

"""
> python fakefiletree.py temp
> ls -lah ./temp
total 35M
drwxr-xr-x 4 vegard vegard 4,0K 2011-09-28 22:02 .
drwxr-xr-x 3 vegard vegard 4,0K 2011-09-28 22:02 ..
drwxr-xr-x 2 vegard vegard 4,0K 2011-09-28 22:02 tmpf-160372
-rw-r--r-- 1 vegard vegard 9,4M 2011-02-17 21:02 tmpf-165459
-rw-r--r-- 1 vegard vegard 5,4M 2011-04-15 22:02 tmpf-19120
drwxr-xr-x 2 vegard vegard 4,0K 2011-09-28 22:02 tmpf-391976
-rw-r--r-- 1 vegard vegard 9,4M 2011-02-03 21:02 tmpf-544825
-rw-r--r-- 1 vegard vegard 1,1M 2011-07-03 22:02 tmpf-776307
-rw-r--r-- 1 vegard vegard 9,6M 2011-08-27 22:02 tmpf-834646

> python old_and_large.py -p '/home/vegard/workspace/Oblig 5/src/temp' -m 10.0 -a 180 -r
Moved file /home/vegard/workspace/Oblig 5/src/temp/tmpf-776307 to /tmp/trash
Moved file /home/vegard/workspace/Oblig 5/src/temp/tmpf-19120 to /tmp/trash
Moved file /home/vegard/workspace/Oblig 5/src/temp/tmpf-834646 to /tmp/trash
Moved file /home/vegard/workspace/Oblig 5/src/temp/tmpf-160372/tmpf-188037 to /tmp/trash
"""