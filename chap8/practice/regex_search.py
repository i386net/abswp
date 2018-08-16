import os
import re
matched_strings = []
# ввод регулярного выражения
user_regex = re.compile(input('Enter you regex: '))

# получить список файлов в директории
for file in os.listdir('./files/'):
    if file[-3:] == 'txt':
        # пройтись по списку файлов
        print(file)
        with open(os.path.join('./files/', file), 'r') as file_obj:
            file_content = file_obj.read()
        matched = user_regex.findall(file_content)
        # если результат регулярного выражения подходит скопировать в список
        matched_strings.append(matched)
# вывести список совпадений на экран или сообщение, что ничего не найдено
print(matched_strings)
