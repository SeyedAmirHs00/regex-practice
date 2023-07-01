import re

ip = 'oreo not a _a2_ Roar took 22'

pat = re.compile(r'\b(\w)(\w*\1)?\b')

ip = pat.sub('X', ip)

print(f'ip is "{ip}"')
