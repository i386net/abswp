import os
# os.rename()
import re

name_regex = re.compile(r'(spam)(\d{3})(\.txt)')
spam_files = []

for file in os.listdir('./spam_dir'):
    file_with_num = name_regex.search(file)
    try:
        spam_files.append(file_with_num.group(2))
    except AttributeError:
        pass
spam_files.sort()
for s in spam_files:
    print(s)


