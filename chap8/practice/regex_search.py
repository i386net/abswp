import os
import re
matched_strings = []
#  ввод регулярного выражения
#message = input(u'Enter you regex: ')
user_regex = re.compile(input(r'Enter you regex: '))

# получить список файлов в директории
for file in os.listdir('./files/'):
    if file[-3:] == 'txt':
        # пройтись по списку файлов
        with open(os.path.join('./files/', file), 'r') as file_obj:
            file_content = file_obj.read()

            ms = user_regex.findall(file_content)
            # если результат регулярного выражения подходит скопировать в список
            matched_strings.append(ms)
# вывести список совпадений на экран или сообщение, что ничего не найдено
print(matched_strings)
for i in range(0):
    print(i)