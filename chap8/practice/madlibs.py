# открыть файл
# подсчитать кол-во и тип ключевых слов
# получить значения от пользователя по кол-ву и типу ключевых слов

# заменить ключевые слова значениями от пользователя
# записать полученный текст в файл

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
# print(words_found)

# print(file_obj)
#  заменить ключевые слова значениями от пользователя

lst = file_obj.split()
for l in range(len(lst)):
    for n in range(len(words_found)):
        for word in words_found:
            for key in word.keys():
                if lst[l].strip(',.') == key:
                    lst[l] = word[key]
                    del words_found[n]
# print(lst)
# print(' '.join(lst))
# записать полученный текст в файл
file = open('madlibs.txt', 'w')
# file.write('\n')
file.write(' '.join(lst))
file.close()
