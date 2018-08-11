import re

password = input('>>> ')


def test_password(psw):
    pass_regex = re.compile(r'^'  # start
                            r'(?=.*[A-Z].*[A-Z])'  # check if password has 2 Uppercase letters
                            r'(?=.*[0-9].*[0-9])'  # check if passord has at least 3 lowercase letters
                            r'(?=.*[a-z].*[a-z].*[a-z])'  # check if password has at least 3 digits
                            r'.{8,}'  # password has len >= 8
                            r'$',  # end
                            re.VERBOSE)
    if pass_regex.search(psw):
        print('Password is strong')
    else:
        print('Password is weak')


test_password(password)
