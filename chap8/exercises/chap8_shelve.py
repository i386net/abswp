import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
print('shelve keys: ', list(shelfFile.keys()))
print('shelve values:', list(shelfFile.values()))

shelfFile.close()

