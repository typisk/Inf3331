"""Find all numbers in a string."""
import re
r1 = r"[+\-]?\d+[.]?\d*" 
r2 = r"[+\-]?\.\d+"     #
r3 = r"[+\-]?\d\.\d+[Ee][+\-]\d\d?"
r = r"(" + r3 + "|"+ r2 +"|"+ r1 + r")" # test for most complicated pattern first
c = re.compile(r)
s = "an array: (1)=3.9836, (2)=4.3E-09, (3)=8766, (4)=.549"
numbers = c.findall(s)
# make dictionary a, where a[1]=3.9836 and so on:
a = {}
for i in range(0,len(numbers)-1,2):
    a[int(numbers[i])] = float(numbers[i+1])
sorted_keys = a.keys(); sorted_keys.sort()
for index in sorted_keys:
    print "[%d]=%g" % (index,a[index])