import re

cc_regex = re.compile(r'''(
                            (\d{4})
                           (-|\.|\s)
                           (\d{4})
                           (-|\.|\s)
                           (\d{4})
                           (-|\.|\s)
                           (\d{4})
                          )
                           ''', re.VERBOSE)

cc_numbers = '''
Credit cards:
4562-1234-4567-8905
1234-2222-2222-2222
4444-4444-4444-4444
'''

card = re.sub(r'[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}',
              r'****-****-*****-***',
              cc_numbers)
print(card)

