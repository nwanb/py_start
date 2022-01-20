f=open('rt5g.txt', 'r')
words=f.read().split()
f.close()
for word in words:
    with open('rt5g_word.txt', 'a') as out:
        out.write(word + '\n')

