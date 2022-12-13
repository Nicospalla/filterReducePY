import random
import functools


def main():
    print(crearLista())


def crearLista():
    lista = ()
    for i in range(20):
        lista = lista + (random.randint(1, 20),)
    print(lista)

    lista = filter(lambda x: x % 2 != 0, lista)
    lista = list(lista)
    print(lista)

    lista = functools.reduce(lambda x, y: x+y, lista)

    return lista


if __name__ == '__main__':
    main()
