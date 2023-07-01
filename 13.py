import re

date1 = '2012-03-30'
date2 = '2020-04-03'

pat = re.compile('(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)')
date1 = pat.sub('\g<month>-\g<day>-\g<year>', date1)
date2 = pat.sub('\g<month>-\g<day>-\g<year>', date2)

print(f'date1 is {date1}')
print(f'date2 is {date2}')
