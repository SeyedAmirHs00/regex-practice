import re

row1 = 'rohan,75,89'
row2 = 'rose,88,92'

pat = re.compile(r'(?P<name>\w+),(?P<math>\w+),(?P<phy>\w+)')

row1_dict = pat.match(row1).groupdict()
row2_dict = pat.match(row2).groupdict()

print(f'row1_dict is "{row1_dict}"')
print(f'row2_dict is "{row2_dict}"')
