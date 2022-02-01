import os, stat, datetime, logging
logging.basicConfig(filename='rt5g_log.log', filemode='w', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
logging.info('Start loging')
log=logging.getLogger('ex')
try:
    input_file='rt5g.txt'
    os.path.isfile(input_file) == True # проверяем есть ли файл
    f=open(input_file, 'r') #открываем файл с текстом
    log_file=open('rt5g_log.log', 'a')
    if f.closed == True:  #Если файл оказался закрыт
        print(datetime.datetime.now(),'Input file', input_file, 'closed')
    else:   #Если он открыт (время, размер, права)
        print(datetime.datetime.now(),': Input file', input_file, 'open,', 'File size input file', input_file,':',  os.stat(input_file).st_size, 'byte,', 'Permissions for input file', input_file, ':', stat.filemode(os.stat(input_file).st_mode), '(',oct(os.stat(input_file).st_mode)[-3:],')', file=log_file)
    words=f.read().split() #читаем файл в переменную , при этом разделяя строку на слова по пробельным символам
    f.close() #закрываем файл чтобы не жрал ресурс
    output_file='rt5g_word.txt'
    with open('rt5g_word.txt', 'a') as out_file:
        if out_file.closed == True:
            print('Output file', output_file, 'closed', file=log_file)
        else:
            print(datetime.datetime.now(), ': Output file', output_file, 'open,', 'Initial file size output file', output_file, ':',
              os.stat(output_file).st_size, 'byte,', 'Permissions for output file', output_file, ':',
              stat.filemode(os.stat(output_file).st_mode), '(', oct(os.stat(output_file).st_mode)[-3:], ')',
              file=log_file)
            out_file.writelines('\n'.join(words))
    if out_file.closed == True:
        print(datetime.datetime.now(), ': Output file', output_file, 'closed,', 'File size output file', output_file, ':',
              os.stat(output_file).st_size, 'byte,', 'Permissions for output file', output_file, ':',
              stat.filemode(os.stat(output_file).st_mode), '(', oct(os.stat(output_file).st_mode)[-3:], ')',
              file=log_file)
    else:
        print('Output file', output_file, 'still open', file=log_file)
except:
   logging.error('Error')
finally:
    log_file.close()