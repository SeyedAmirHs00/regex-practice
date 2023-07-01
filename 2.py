import re

items = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']

items = [re.sub('e', 'X', x) for x in items if re.fullmatch('h.*', x)]

print(f'items is {items}')