import re

words = ['sequoia', 'subtle', 'exhibit',
         'a set', 'sets', 'tests', 'site', 'semester']

pat = re.compile('s.*(e.*t|t.*e).*')
words = [word for word in words if pat.fullmatch(word)]
print(f'words is {words}')
