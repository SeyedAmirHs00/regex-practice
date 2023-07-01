import re

ip = 'a+42//5-c pressure*3+42/5-14256'

ip = re.sub(r'42//?5', '8', ip)

print(f'ip is "{ip}"')