a = 'valor' # True
a = 0 # False
a = -0.000001 # True
a = '' # False
a = ' ' # True
a = [] # False
a = {} # False

if a:
    print('Existe')
else:
    print('Não existe ou zero ou vazio...')