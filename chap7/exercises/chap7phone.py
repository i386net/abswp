import re

phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phone_num_regex.search('My number: 333-111-2345')
print('Phone number:', mo.group())

# создание групп регулярных выражений
phone_num_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phone_num_regex.search('My number: 333-111-2345')
print('Code:', mo.group(1))
print('Number:', mo.group(2))
print('Full number:', mo.group(0))

# извлечение всех групп
print(mo.groups())
area_code, main_number = mo.groups()
print('area code:', area_code)
print('main number:', main_number)

# поиск скобок
phone_num_regex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo1 = phone_num_regex.search('My number: (812) 555-1123')
print(mo1.groups())

# поиск необязательных символов
phone_num_regex = re.compile('(\d{3}-)?\d{3}-\d{4}')
mo1 = phone_num_regex.search('number1: 916-555-1123')
mo2 = phone_num_regex.search('number2: 555-2233')
print('number1:', mo1.group())
print('number2:', mo2.group())

# метод findall
phone_num_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo1 = phone_num_regex.findall('mobile: 345-545-4545 office: 999-345-3465')

print(mo1)

phone_num_regex = re.compile(r'\(?\d{3}\)?\W?\d{3}\W?\d{4}')
mo1 = phone_num_regex.findall('num1: 111-222-2222'
                             'num2: (222)2222222'
                             'num3: (333)-333-3333')
print(mo1)


