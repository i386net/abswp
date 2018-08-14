import os

path = os.getcwd()

print('basename: ', os.path.basename(path))
print('dirname: ', os.path.dirname(path))

print(os.path.split(path))

path = 'usr/bin'.split(os.path.sep)
print(path)

print(os.getcwd().split(os.path.sep))
