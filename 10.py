import re

ip = 'a<apple> 1<> b<bye> 2<> c<cat>'

pat = re.compile('<.+?>')

items  = pat.findall(ip)

print(f'items is {items}')