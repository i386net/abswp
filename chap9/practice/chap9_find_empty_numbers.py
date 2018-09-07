import os
import re

name_regex = re.compile(r'(spam)(\d{3})(\.txt)')
file_dir = './spam_dir'
os.chdir(file_dir)
for prev_file in sorted(os.listdir('.')):
    for file in sorted(os.listdir('.')):
        prev_file_num_rex = name_regex.search(prev_file)
        file_num_rex = name_regex.search(file)
        prev_num = prev_file_num_rex.group(2)
        file_num = file_num_rex.group(2)
        if int(file_num) - int(prev_num) == 2:
            new_num = int(prev_num) + 1
            new_name = file.replace(file_num, '00' + str(new_num))
            # os.replace(file, new_name)
            print(file, new_name)

