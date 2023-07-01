import re

ip = 'wow:Good:2_two.five: hi-2 bye kite.777:water.'

pat = re.compile(r'(\w+)[.:](?:\w+[.:])+(\w+)[.:]')

ip = pat.sub(r'\g<2>-\g<1>', ip)
print(ip)
