bienv = input('¿Cunato es 2 + 2?\n')

while bienv != '4':
    print('Nop')
    bienv = input('Desea realizar otro intento? [Y/N]\n')
    if bienv in 'Nn':
        print('cya')
        break
    else:
        print('lo tomare como un si')
    bienv = input('¿Cuanto es 2 + 2?\n')
if bienv == '4':
    print('buena pa')
