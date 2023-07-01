import re

row1 = 'name:rohan,maths:75,phy:89,'
row2 = 'name:rose,maths:88,phy:92,'

pat = re.compile(r'(\w+):(\w+)')

row1_dict = {x[1]: x[2] for x in pat.finditer(row1)}
row2_dict = {x[1]: x[2] for x in pat.finditer(row2)}

print(f'row1_dict is {row1_dict}')
print(f'row2_dict is {row2_dict}')
