# собственный словарь символов
import re
vowel_regex = re.compile(r'[aeiouAEIOU]')
vo = vowel_regex.findall('Robocop eats baby food. BABY FOOD.')
print(vo)