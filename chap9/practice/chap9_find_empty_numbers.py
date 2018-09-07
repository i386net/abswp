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


'''
import os
# os.rename()
import re
import shutil

name_regex = re.compile(r'(spam)(\d{3})(\.txt)')
spam_files_nums = []


for prev_file in sorted(os.listdir('./new_dir')):
	for file in sorted(os.listdir('./new_dir')):
		prev_file_num_rex = name_regex.search(prev_file)
		file_num_rex = name_regex.search(file)
		#print(prev_file_num_rex.group(2), file_num_rex.group(2))
		prev_num = prev_file_num_rex.group(2)
		file_num = file_num_rex.group(2)
		print(prev_num, file_num)
		if int(file_num) - int(prev_num) > 1:
			new_num = int(prev_num) + 1
			print('new {} name is {}'.format(file, file.replace(file_num, '00' + str(new_num))))
			new_name = file.replace(file_num, '00' + str(new_num))
			os.rename(file, new_name)
'''
