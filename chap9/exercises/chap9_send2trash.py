import send2trash
try:
    send2trash.send2trash('backup_of_backups')
except:
    print('No such file or directory.')
