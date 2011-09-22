import re

ifile = open('jhead.sample', 'r').read() # proof of concept

def gettime(item):
    match = r"(\d{4}):(\d{2}):(\d{2})\s+(\d{2}):(\d{2}):(\d{2})" #pattern
    y = re.findall(match, item)[1] #get last match
    return  (",".join(y[0:3]), ",".join(y[3:6])) # return two tuple of strings
    #example format: ('2002,05,19', '18,10,03')

def prefix(tuples, imagename):
    string = ""
    for item in tuples: #go through the tuple
        string += item.replace(',','_') + "__" #replace comma with underscore. add two underscores at the end
    return (string + imagename)
prefixed = prefix(gettime(ifile), 'img_4911.jpg')
print prefixed #or just call os.rename

"""
python jgpegrename.py
2002_05_19__18_10_03__img_4911.jpg
"""
