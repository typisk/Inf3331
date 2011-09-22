import re
loop1 = '[0:12]'
loop2 = '[0:12, 4]'

r1 = r'\[(.+):(.+?),?(.*)\]'
r2 = r'\[(.+):(.+),?(.*)\]'

r3 = r'\[(\d+):(\d+)\,?\s?(\d+)?\]'

print re.search(r3, loop1).groups()
print re.search(r3, loop2).groups()
