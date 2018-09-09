import os
import re

name_regex = re.compile(r'(spam)(\d+)(\.txt)')
file_dir = './spam_dir'
os.chdir(file_dir)
file_dir_lst = os.listdir()
file_dir_lst.sort()

for i, file in enumerate(file_dir_lst, start=1):
    num_r = name_regex.search(file)
    num = num_r.group(2)
    if i != int(num):
        new_name = file.replace(num, '00{}'.format(i))
        print(i, new_name)
        os.rename(file, new_name)

