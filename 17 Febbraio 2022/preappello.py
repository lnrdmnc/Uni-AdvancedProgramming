"""

Scrivere nella classe C, fornita nel file esercizio1.py, un metodo di classe aggiungiProprieta che
per ciascuna variabile di classe di C di tipo str, crea una property con lo stesso nome della
variabile. Il setter della property deve effettuare l’assegnamento solo se il valore da assegnare
è una stringa. In caso contrario deve lanciare TypeError con argomento la stringa “Non e`
possibile assegnare {} alla variabile {}” dove al posto delle parentesi graffe devono comparire il
valore e il nome passati al setter.  


"""
"""
from ast import arg
from multiprocessing.sharedctypes import Value
import string
from xmlrpc.client import Boolean

class C:

    @classmethod
    def aggiungiProprieta(cls,*args,**kwargs)-> Boolean:
        privateName = {}
        for arg in args:
            privateName[arg] = "_" + str(arg)

        def setter(name, value):
            if(type(value) is not str):
                raise TypeError(f'Non e`possibile assegnare {value} alla variabile {privateName}')
            setattr(cls, privateName[name], value)
            return True

        def getter():
            return getattr(cls, privateName)

        for arg in args:
            setattr(cls, privateName[arg], property(fget= getter, fset= setter))
c=C()
c.aggiungiProprieta('test1', 'test2')

c.test1 = 0
c.test2 = 11

print(c.test1,c.test2)
"""


"""
Scrivere nel file esercizio2.py un decorator factory dFact che restituisce un decoratore di
funzione che “trasforma” la funzione f in un generatore che all’i-esima invocazione di next
restituisce il valore ottenuto invocando f con gli argomenti ottenuti sommando L[i] a tutti gli
argomenti con cui la funzione f è invocata originariamente. Se la suddetta somma causa
un’eccezione TypeError allora il generatore smette di restituire valori. 


"""

"""
from fileinput import close
from functools import wraps


def decorator_factory(n:int):
        
    def decorator(fun):
            @wraps(fun)
            def wrapper(*args,**kwargs):
                try:
                    l=[]
                    for i in range(n):
                        l.append(fun(*args))
                        yield sum(l)
                except Exception:
                    yield
            return wrapper

    return decorator


@decorator_factory(1)
def somma(*args):
    return sum(args)

for i in somma(1,'ciao',2,3):
    print(i)
    
"""

"""
Scrivere nel file esercizio2.py un decoratore di classe decoraClasse che aggiunge alla classe
decorata il metodo conQualiArgomenti che restituisce una tupla contenente
• i valori di tutti gli argomenti posizionali (compresi quelli variabili)
• le coppie (chiave, valore) di tutti gli argomenti keyword (compresi quelli variabili)
passati all’ultima invocazione di __init__ .

"""
from copy import deepcopy

def decoraClasse(cls):
    
    oldInit=cls.__init__

    def ___newInit___(self,*args,**kwargs):

        cls.privateArgs=deepcopy(args)
        cls.privateDict=deepcopy(kwargs)
        oldInit(self,*args,**kwargs)

    cls.__init__=___newInit___

    @classmethod
    def conQualiArgomenti(cls):
        return (cls.privateArgs,cls.privateDict)

    cls.conQualiArgomenti=conQualiArgomenti
    return cls


@decoraClasse
class Classe:
    
    def __init__(self,*args,**kwargs):
        pass
        
if __name__ == '__main__':
    x= Classe(1,2,3)
   # x= Classe(1,2,4, kwarg1=3, kwarg2=6)
    print(x.conQualiArgomenti())














































'''
class C:

    @classmethod
    def aggiuggiProprieta(cls, name):
        privateName = "__" + name

        def setter(name, value):
            if (value is not str):
                raise AttributeError("impossibile assegnare {} alla variabile {}".format(value, name))
            setattr(cls, privateName, value)

        def getter():
            return getattr(cls, privateName)
        setattr(cls, name, property(fget= getter, fset= setter))


x = C()
x.aggiuggiProprieta("lol")
x.lol = 5
'''
