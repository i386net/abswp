import os
import shutil
txt = '''
1234
5678
91011
'''
if not os.path.exists('./tmp'):
    os.makedirs('./tmp/')
    file = open('testfile.txt', 'w')
    file.write(txt)
    file.close()
shutil.copy('testfile.txt', './tmp/')
print(shutil.copy('testfile.txt', './tmp/testfile2.txt'))  # return string with new path

print(shutil.copytree('./tmp', './tmp_backup'))

