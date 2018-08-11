# символ .  - любой одиночный символ за исключением символа новой строки

import re

at_regex = re.compile(r'.at')
at = at_regex.findall('Tha cat in the hat sat on the flat mat.')
print(at)

name_regex = re.compile(r'First name: (.*) Last name: (.*)')
n = name_regex.search('First name: Robot1 Last name: VErter')
print(n.groups())

#  ограничение режима .* с помощью знака ?

nongreedy_regex = re.compile(r'<.*?>')
n = nongreedy_regex.search('<To serve man> for dinner')
print(n.group())

greedy_regex = re.compile(r'<.*>')
g = greedy_regex.search('<To serve man> for dinner>')
print(g.group())

