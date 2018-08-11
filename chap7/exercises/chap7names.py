import re


hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = hero_regex.search('Tina Fey and Batman')
print(mo2.group())
print(mo1.groups())

# каналы

bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search("Batmobile looses it's wheel")
print(mo.group())
print(mo.group(1))

# поиск необязательных символов
bat_regex =re.compile('Bat(wo)?man')
mo1 = bat_regex.search('The Adventures of Batman')
mo2 = bat_regex.search('The Adventures of Batwoman')
print(mo1.group())
print(mo2.group())

# совпадение с нулевым или большим кол-м экземпляров

bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search('the adventures of Batman')
print('name1:', mo1.group())

mo2 = bat_regex.search('the adventures of Batwoman')
print('name2', mo2.group())

# совпадение с одним или большим кол-м экземпляров

bat_regex = re.compile(r'Bat(wo)+man')
mo1 = bat_regex.search('the adventures of Batwowowoman')
mo2 = bat_regex.search('the adventures of Batman')
print(mo1.group())
if mo2 is None:
    print('True')
