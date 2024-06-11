#Ejercicio 8.11: Funciones y documentación

def valor_absoluto(n):
    '''
    Esta función calcula el valor absoluto de un número.
    
    pre: n es un número Real
    pos: devuelve el valor absoluto de n
    '''
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(l):
    
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

def veces(a, b):
    '''
    La función suma "b" veces el numero "a"
    
    pre: b>=0
    pos: devuelve b*a
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

def collatz(n):
    '''
    La función...?

    pre: n>1
    pos:...?
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
            print(n)
        else:
            n = 3 * n + 1
            print(n)
        res += 1

    return res
