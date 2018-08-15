import os

print(os.path.exists('/usr/bin'))
print(os.path.exists('c:\\windows'))

print(os.path.isdir('/Volumes'))
print(os.path.isfile('/Applications/Utilities/Grab.app'))
print(os.path.isfile('/usr/bin/zip'))
print(os.path.isdir('usr/bin/zip'))

print(os.path.exists('/Volumes/Kino'))