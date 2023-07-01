import re

words = 'bred red spread credible red.'

words = re.sub(r'\bred\b', 'brown', words)

print(f'words is "{words}"')
