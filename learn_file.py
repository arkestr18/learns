namefile = input('введите имя файла')
text = input('введите текст в этом файле')

file = open(namefile, 'w')
file.write( text )

file.close()