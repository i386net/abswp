# добавление комментариев в сложные рег выражения с помощью многострочного синтаксиса и метода
# re.VERBOSE

import re

phone_regex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?
                        (\s|-|\.)?
                        \d{3}
                        (\s|-|\.)?
                        \d{4}
                        (\s*(ext|x|ext.)\s*\d{2,5})?
)''', re.VERBOSE)

n = phone_regex.findall('(456) 456 3456, 456-345-3456, 555 6677')
for number in n:
    print('• {:<20}'.format(number[0]))


