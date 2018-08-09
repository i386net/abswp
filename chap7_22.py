import re

text = '''
Alice eats apples.
Bob pets cats.
Carol throws baseballs.
Alice throws Apples.
BOB EATS CATS.
---
Robocop eats apples.
ALICE THROWS FOOTBALLS.
Carol eats 7 cats.'''

names_regex = re.compile(r'^(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.$',
                         re.IGNORECASE | re.MULTILINE)
for name in names_regex.findall(text):
    print(*name)
