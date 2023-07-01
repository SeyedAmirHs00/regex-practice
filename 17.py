import re

anchor1 = '# <a name="regular-expressions"></a>Regular Expressions'
anchor2 = '## <a name="subexpression-calls"></a>Subexpression calls'

pat = re.compile(r'[^"]*"(.+)"></a>(.+)')

anchor1 = pat.sub(r'[\2](#\1)', anchor1)
anchor2 = pat.sub(r'[\2](#\1)', anchor2)

print(f'anchor1 is "{anchor1}"')
print(f'anchor2 is "{anchor2}"')
