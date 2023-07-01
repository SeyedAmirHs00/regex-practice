import re

str1 = 'def factorial()'
str2 = 'a/b(division) + c%d(#modulo) - (e+(j/k-3)*4)'
str3 = 'Hi there(greeting). Nice day(a(b)'

pat = re.compile(f'\([^(]*?\)')
str1 = pat.sub('', str1)
str2 = pat.sub('', str2)
str3 = pat.sub('', str3)


print(f'str1 is "{str1}"')
print(f'str2 is "{str2}"')
print(f'str3 is "{str3}"')
