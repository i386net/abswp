# знак $ и ^ для указания позиции искомого выражения
# ^ позиция в начале текста, $ позиция в конце текста

import re

begins_regex = re.compile(r'^Hello')
b = begins_regex.search('Hello world')
print(b.group())


b = begins_regex.search('He said hello.')
print(b)

ends_regex = re.compile(r'\d+$') # same as \d{2}
e = ends_regex.search('your number is 43')
print('e', e)
print(e.group())


whole_regex = re.compile(r'^\d+$')
w = whole_regex.search('12234545')
w2 = whole_regex.search('1234jkj4545')
print('w', w)
print('w2', w2)
