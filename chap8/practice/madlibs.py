# The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.

# открыть файл
file = open('madlibs.txt', 'r')
key_words = ['ADJECTIVE', 'NOUN', 'VERB']
words_found = []
file_obj = file.read()
file.close()

# сформировать список словарей ключевых слов с пустыми значениями
for word in file_obj.split():
    if word.strip(',.') in key_words:
        words_found.append({word.strip(',.'): ''})

# получить замены от пользователя в внести их в список словарей
# вместо пустых значений
for word in words_found:
    for k in word.keys():
        word[k] = input('Enter {}: '.format(k))

#  заменить ключевые слова значениями от пользователя
lst = file_obj.split()
for l in range(len(lst)):
    for n in range(len(words_found)):
        for word in words_found:
            for key in word.keys():
                if lst[l].strip(',.') == key:
                    if lst[l].endswith('.'):
                        lst[l] = word[key] + '.'
                    elif lst[l].endswith(','):
                        lst[l] = word[key] + ','
                    else:
                        lst[l] = word[key]
                    del words_found[n]

# записать полученный текст в файл
file = open('madlibs.txt', 'w', encoding='UTF-8')
file.write(' '.join(lst))
file.close()
