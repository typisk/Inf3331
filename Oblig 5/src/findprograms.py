import os, sys

def findprograms(rest):
    ret = {}
    path = os.environ['PATH'] #finds all paths in system
    paths = path.split(os.pathsep) #splits the paths
    for program in rest:    #check each program
        program_path = None
        for d in paths:     #for each path in system
            if os.path.isdir(d):    #check if path is a directory
                fullpath = os.path.join(d, program) #finds the full path in system
                if sys.platform[:3] == 'win':       # if windows
                    for ext in '.exe', '.bat':
                        if os.path.isfile(fullpath + ext):  #if program found
                            program_path = d;           #found program!
                else:       #if not windows
                    if os.path.isfile(fullpath):    #if program found
                        program_path = d;       #found program!
        if program_path:    #If program path is not None
            ret[program] = True; #then program exist
        else: #or program does not exist
            ret[program] = False;
    return ret;
        
        


programs = {
  'gnuplot'  : 'plotting program',
  'gs'       : 'ghostscript, ps/pdf interpreter and previewer',
  'f2py'     : 'generator for Python interfaces to F77',
  'swig'     : 'generator for Python interfaces to C/C++',
  'convert'  : 'image conversion, part of the ImageMagick package',
  }
installed = findprograms(programs.keys())
for program in installed.keys():
    if installed[program]:
        print "You have %s (%s)" % (program, programs[program])
    else:
        print "*** Program %s was not found on the system" % (program,)
        
"""
python findprograms.py

*** Program convert was not found on the system
You have gs (ghostscript, ps/pdf interpreter and previewer)
*** Program swig was not found on the system
*** Program gnuplot was not found on the system
You have f2py (generator for Python interfaces to F77)
"""