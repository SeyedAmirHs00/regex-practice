import re

cast = 'dragon-unicorn--centaur---mage----healer'
c = '-'
cast = re.sub(rf'{c}{{3,}}', c, cast)
print(f'cast is "{cast}"')
