import os
# os.rename()
import re

name_regex = re.compile(r'(spam)(\d{3})(\.txt)')
spam_files_nums = []

for file in os.listdir('./spam_dir'):
    file_with_num = name_regex.search(file)
    try:
        spam_files_nums.append(file_with_num.group(2))
    except AttributeError:
        pass
spam_files_nums.sort()
for s in spam_files_nums:
    print(s)

