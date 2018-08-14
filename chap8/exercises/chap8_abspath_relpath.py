import os

print(os.path.abspath('.'))

print(os.path.abspath('./Scripts'))

print(os.path.isabs('.'))

print(os.path.isabs(os.path.abspath('.')))

print(os.path.isabs('/users/'))


print(os.path.relpath('/users', '/'))
print(os.path.relpath('/users', '/tmp/tnt25109/'))
print(os.path.relpath('/tmp/tnt25109/'))
