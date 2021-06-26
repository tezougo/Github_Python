lista = []


def inseri_elementos(grupo, element):
    if len(grupo) == 0:
        grupo.append(element)
        return grupo
    else:
        for i in range(len(grupo)):
            if grupo[i] == element:
                print('já tem o elemento:\n{}'.format(grupo[i]))
                break
        if grupo[i] != element:
            grupo.append(element)
    print('Elementos na lista: ')
    return grupo
print(inseri_elementos(lista, 10))
print(inseri_elementos(lista, 1331))
print(inseri_elementos(lista, 10))
print(inseri_elementos(lista, 10))
print(inseri_elementos(lista, 10))
print(inseri_elementos(lista, 11))
