import re

s1 = 'amir_ali_hossein_taghi'
s2 = 'python_java_cpp'
s3 = 'asghar_akbar_soghra_kobra'

def camel_case_sub_func(x):
    return x[1] + x[2].upper()

s1 = ''.join([x.capitalize() for x in re.split('_', s1)])
s2 = ''.join([x.capitalize() for x in re.split('_', s2)])
s3 = ''.join([x.capitalize() for x in re.split('_', s3)])

print(f's1 is "{s1}"')
print(f's2 is "{s2}"')
print(f's3 is "{s3}"')
