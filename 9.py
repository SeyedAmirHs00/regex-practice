import re
import math

s1 = 'first-3.14'
s2 = 'next-123'


def log_sub_func(x):
    return '-' + str(math.log(float(x[1])))


pat = re.compile('-(.*)')
s1 = pat.sub(log_sub_func, s1)
s2 = pat.sub(log_sub_func, s2)

print(f's1 is "{s1}"')
print(f's2 is "{s2}"')
