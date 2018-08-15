# open all txt files and find there string with user's regex
#  ввод регулярного выражения
# получить список файлов в директории
# пройтись по списку файлов
# если результат регулярного выражения подходит скопировать в список
# вывести список совпадений на экран или сообщение, что ничего не найдено

import os
import re

user_regex = input(r'Enter you regex: ')

