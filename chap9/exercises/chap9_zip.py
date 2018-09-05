import zipfile, os

os.chdir('c:\\users\\admin\\desktop\\')
for file in os.listdir():
    if file.endswith('zip'):
        print('|-- ' + file)
exampleZip = zipfile.ZipFile('Bot-windows.zip')
for name in exampleZip.namelist():
    print(name)
    fileInfo = exampleZip.getinfo(name)
    print('\tfile size: ' + str(fileInfo.file_size) + 'B')
    print('\tcompressed file size: ' + str(fileInfo.compress_size) + 'B')
exampleZip.close()

exampleZip = zipfile.ZipFile('Bot-windows.zip')
os.makedirs('./win_bot')
exampleZip.extractall('./win_bot')
exampleZip.close()

os.chdir('c:\\users\\admin\\desktop\\')
zipFile = zipfile.ZipFile('win_bot.zip', 'a')
print(os.getcwd())
for folder, subfolders, files in os.walk('./win_bot'):
    for file in files:
        print('compressing >>> ' + os.path.join(folder, file))
        zipFile.write(os.path.join(folder, file), compress_type=zipfile.ZIP_DEFLATED)
zipFile.close()
