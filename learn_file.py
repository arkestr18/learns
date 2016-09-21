file = open('test.txt')
print((file.read()) + str((len(file.read()))))
file.close()