import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# TODO сохранение содержимого буфера обмена
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] == pyperclip.paste()
elif len(sys.argv) == 2:
    pass
    # TODO  Сформировать список ключевых слов и загрузить содержимое



mcbShelf.close()