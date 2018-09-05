import os
import shutil
try:
    os.chdir('..')
    os.unlink('settings.txt')
except:
    print('No such file')

try:
    os.chdir('./exercises')
    shutil.rmtree('tmp')
except:
    print('No such directory')
