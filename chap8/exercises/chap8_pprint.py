import pprint

cats = [
    {'name': 'Zophie', 'desc': 'chubby'},
    {'name': 'Pooka', 'desc': 'fluffy'}
]
print(cats)
print(pprint.pformat(cats))
fileobj = open('myCats.py', 'w')
fileobj.write('cats = ' + pprint.pformat(cats) + '\n')
fileobj.close()