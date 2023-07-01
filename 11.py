import re

words = ['sequoia', 'attest', 'tattletale', 'asset']

words = [re.subn('t', 't', x) for x in words]
print(f'wrods is {words}')
