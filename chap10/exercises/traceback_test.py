import traceback

try:
    raise Exception('This is error message')
except:
    error_file = open('error_file.txt', 'w')
    error_file.write(traceback.format_exc())
    error_file.close()
    print('Information about error was written to error_file.txt')
