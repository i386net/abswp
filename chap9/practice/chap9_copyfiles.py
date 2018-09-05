# copy files with ext to new folder

import os
import shutil
import sys


def copy_to_folder():

    # ввод расширения, пути исх папки и папки назначения
    ext = input('Enter the file extention: ')
    # исх папка
    source = input('Enter the full path to source folder: ')
    while not os.path.isabs(source):
        source = input('Enter the correct source folder: ')
    if not os.path.exists(source):
        print('No such directory was found. ')
        sys.exit('Bye-bye')
    # папка назначения
    destination = input('Enter the full path to destionation folder: ')
    # проверка
    while not os.path.isabs(destination):
        destination = input('Enter the correct path to destionation folder: ')

    if not os.path.exists(destination):
        print('Creating folder: ' + destination)
        os.makedirs(destination)
    # поиск файлов с нужным расширением
    cfl = []
    for root, subdirs, files in os.walk(source):
        for file in files:
            if file.endswith(ext):
                print('Copy ' + os.path.join(source, file) + ' to ' + destination)
                shutil.copy(os.path.join(source, file), destination)
                cfl.append(file)
    if len(cfl) > 0:
        print('These files were copied: ')
        for file in cfl:
            print('° ', file)
    else:
        print('No files were copied.')


copy_to_folder()

