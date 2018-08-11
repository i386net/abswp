def strip_string(string, *symbols):
    import re

    if len(symbols) == 0:
        # поиск пробелов в начале и конце строки
        newstring = re.sub(r'(^\s*)', '', string)
        newstring = re.sub(r'(\s*$)', '', newstring)
        return newstring
    else:
        # поиск произвольных символов
        s = ''.join(symbols)
        pattern = '[' + s + ']'
        return re.sub(pattern, '', string, flags=re.IGNORECASE)


if __name__ == '__main__':
    s = input('String >>> ')
    symbs = input('Enter symbols to remove(optinal) >>> ')
    print(strip_string(s, *symbs))
