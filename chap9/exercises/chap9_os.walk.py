import os

for folder, subfolders, files in os.walk('../../chap8'):
    # print(folder)
    # print(subfolders)
    # print(files)
    print('Current folder is: ' + os.path.abspath(folder))
    for subfolder in subfolders:
        print('Subfolder of folder: ' + os.path.abspath(folder) + ': ' + subfolder)
    for file in files:
        print('\t\t|-- ' + file)
