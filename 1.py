import  re

s1 = 'creed refuse removed read'  
s2 = 'refused reed redo received'

pat = re.compile('removed|reed|received|refused')
s1 = pat.sub('X', s1)
s2 = pat.sub('X', s2)

print(f's1 is "{s1}"')
print(f's2 is "{s2}"')