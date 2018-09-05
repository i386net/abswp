# find files wich are more than 100 Mb

import os
import sys

path = input('Please, enter the correct path >>> ')
tottal = 0
for root, subfolders, files in os.walk(path):
    for file in files:

        try:
            full_file_name = os.path.join(root, file)
            if os.path.getsize(full_file_name) > 100 * (1024 ** 2):
                tottal += os.path.getsize(full_file_name)
                print('File {} — {:n} Mb'.format(full_file_name, os.path.getsize(full_file_name)/(1024 ** 2)))
        except FileNotFoundError:  # dont show errors on dot files
            pass
print('Tottal size is {:n} Gb'.format(tottal/(1024 ** 3)))
