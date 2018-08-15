path = '/users/dk-mac/hello.txt'
path2 = '/users/dk-mac/sonnet29.txt'
helloFile = open(path2, 'w')
helloFile.write("""When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
""")

helloFile = open(path, 'r')
helloContent = helloFile.read()
print(helloContent)

sonnetFile = open(path2, 'r')
for line in sonnetFile.readlines():
    print(line, end='')





