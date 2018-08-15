import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# сохранение содержимого буфера обмена
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
    # удаление ключа
    if sys.argv[2] in mcbShelf.keys():
        del mcbShelf[sys.argv[2]]
    # удаление всех ключей хранилища
    elif sys.argv[2] == 'all':
        for k in mcbShelf.keys():
            print('deleting %s: %s' % (k, mcbShelf[k]))
            del mcbShelf[k]
elif len(sys.argv) == 2:
    # Сформировать список ключевых слов и загрузить содержимое
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()



