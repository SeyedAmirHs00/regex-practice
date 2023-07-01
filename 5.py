import re

s1 = 'AmirAliHosseinTaghi'
s2 = 'PythonJavaCpp'
s3 = 'AsgharAkbarSoghraKobra'

pat = re.compile('([a-z])([A-Z])')
s1 = pat.sub(r'\1_\2', s1).lower()
s2 = pat.sub(r'\1_\2', s2).lower()
s3 = pat.sub(r'\1_\2', s3).lower()

print(f's1 is "{s1}"')
print(f's2 is "{s2}"')
print(f's3 is "{s3}"')
