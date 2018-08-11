# инвертированный словарь символов
import re
consonant_regex = re.compile(r'[^aeiouAEIOU]')
cr = consonant_regex.findall('Robocop eats baby food. BABY FOOD.')
print(cr)