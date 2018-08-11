# константа re.DOTALL для включения всех символов новой строки

import re
message = 'Serve the public trust. \nProtect the innocent. \nUphold the law.'
no_newline_regex = re.compile(r'.*')
nn = no_newline_regex.search(message)
print(nn.group())

newline_regex = re.compile(r'.*', re.DOTALL)
n = newline_regex.search(message)
print(n.group()) 