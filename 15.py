import re

ip = 'sequoia subtle exhibit asset sets2 tests si_te'

pat = re.compile(r'\bs\w*(e\w*t|t\w*e)\w*\b')
ip = pat.sub(r'[\g<0>]', ip)

print(f'ip is "{ip}"')
