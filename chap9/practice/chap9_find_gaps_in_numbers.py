import os
import re

name_regex = re.compile(r'(spam)(\d{3})(\.txt)')
file_dir = './spam_dir'
os.chdir(file_dir)

file_dir = os.listdir()
file_dir.sort()
'''
for smaller_file in sorted(os.listdir('.')):
    for bigger_file in sorted(os.listdir('.')):
        smaller_file_num_rex = name_regex.search(smaller_file)
        bigger_file_num_rex = name_regex.search(bigger_file)
        smaller_num = smaller_file_num_rex.group(2)
        bigger_num = bigger_file_num_rex.group(2)
        if int(bigger_num) - int(smaller_num) >= 2:
            new_num = int(smaller_num) + 1
            new_name = bigger_file.replace(bigger_num, '00' + str(new_num))
            #os.replace(file, new_name)
            print(smaller_file)
            print(bigger_file)
            print(bigger_file, new_name)
'''

for x in range(len(file_dir)):  # smaller num
    for y in range(len(file_dir)):  # bigger num
        smaller_file_num_rex = name_regex.search(file_dir[x])
        bigger_file_num_rex = name_regex.search(file_dir[y])
        smaller_num = smaller_file_num_rex.group(2)
        bigger_num = bigger_file_num_rex.group(2)
        if int(bigger_num) - int(smaller_num) > 1:
            new_num = int(smaller_num) + 1

            new_name = file_dir[y].replace(bigger_num, '00' + str(new_num))
            print('{} {} -> {}'.format(file_dir[x], file_dir[y], new_name))

