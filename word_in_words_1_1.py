import os.path
try:
    os.path.isfile('rt5g.txt') == True # проверяем есть ли файл
    f=open('rt5g.txt', 'r') #открываем файл с текстом
    words=f.read().split() #читаем файл в переменную , при этом разделяя строку на слова по пробельным символам
    f.close() #закрываем файл чтобы не жрал ресурс
    for word in words: #перебираем по переменной words
        with open('rt5g_word.txt', 'a') as out: #открываем (создаем) файл вывода как переменную our
            out.write(word + '\n') #записываем каждое слово построчно:
except:
   print('input file not found')

