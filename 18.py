import re

ip = '''oppressed abandon accommodation bloodless carelessness committed apparition innkeeper occasionally afforded embarrassment foolishness depended successfully succeeded possession cleanliness suppress'''

pat = re.compile(r'\b(?:\w*(\w)\1\w*){2,}\b')

items = [x[0] for x in pat.finditer(ip)]

print(items)
