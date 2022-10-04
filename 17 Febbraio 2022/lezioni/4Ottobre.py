""" 

Rivedere la roba sui lines e name space 
Esercizio: 
Scrivere la classeB che ha il metodo di istanza contaVarClasse(self,t,n):
prende in input un intero t e un intero n

restituisce il numero di variabili di classe di tipo t  delle prime n classi nella gerarchia formata dalla classe cui self è istanza e dalle sue superclassi

le prime n classi secondo l'ordine indicato in __mro__ 
se il numero di classsi nella suddetta gerarchia è minore di n allora vengono considerate tutte le classi della gerarchia

retrospection __dict__

NB gli attributi di una classe, di un istanza o di un modulo sono mantenuti in un dizionario chiamato __dict__ che è sua volta un attributo dell'oggetto

vars restituisce il __dict__ per il modulo, la classe, l'istanza o un qualsiasi altro oggetto dotato di un un attributo __dict__

il namespace di un modulo è mantenuto in __dict__

import sys 
print(sys.modules[__name__].__dict__==vars())

la variabile di classe la vado a prendere dal var oppure dal dict


metodo è quello si invoca sull'oggetto 
metodo di istanza e metodi di classe
la funzione è quella che prende come argomento gli oggetti 
"""

from operator import contains
import sys


class   ClasseB:

    def __init__(self):
        conta=0

    def contaVarClasse(self,t,n):
        mro=ClasseB.__mro__
        for i in mro:
            for arg in vars(i):
                if(type(arg)==t):
                    #print(sys.modules[__name__].__dict__==vars(t))
                    conta+=1
        return conta


class A:
    def __init__(self):
        pass

class B:
    def __init__(self): 
        pass

class C(A,B):
    def __init__(self):
        pass

D=ClasseB(C)
print(D.contaVarClasse(int,10,10,20,30))











