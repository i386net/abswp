import re

names = '''
Satoshi Nakamoto
Alice Nakamoto
Robocop Nakamoto
satoshi Nakamoto
Mr. Nakamoto
Nakamoto
Satoshi nakamoto'''

satoshi_regex = re.compile(r'^[A-Z]\w*\sNakamoto', re.MULTILINE)

for name in satoshi_regex.findall(names):
    print(name)