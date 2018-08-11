# метод sub() принимает два аргумента, первый строка заменяющая найденные совпадения,
# второй строка регулярного выражения
import re
names_regex = re.compile('Agent \w+')
print(names_regex.sub('Censored', 'Agent Alice gave the secret documents to Agent Bob.'))


# подстановка в найденные группы по ссылкам

agentnames_regex = re.compile(r'Agent (\w)\w*')
print(agentnames_regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Boи was a '
                           'double agent.'))
