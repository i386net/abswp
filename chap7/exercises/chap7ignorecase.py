# поиск совпадений независимо от регистра букв

import re

robocop = re.compile(r'robocop', re.IGNORECASE)
r1 = robocop.search('Robocop is part man, part machine, all cop')
r2 = robocop.search('ROBOCOP protects the innocent.')
r3 = robocop.search('Al, why does your programming book talk anout robocop so much?')
print(r1.group(), r2.group(), r3.group())