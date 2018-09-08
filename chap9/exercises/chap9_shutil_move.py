import shutil

print(shutil.move('./tmp_backup', './backup_of_backups/'))
shutil.move('testfile.txt', './backup_of_backups/1/')  # if dir 1 is not exist, testfile.txt -> renamed to 1
