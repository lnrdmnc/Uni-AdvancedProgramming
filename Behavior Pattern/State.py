
"""Design Pattern Comportamentale consente ad un oggetto di modificare il proprio comportamento quando il suo stato interno cambia

E' utile nei seguenti casi:
Quando il comportamento di un oggetto dipende dal suo stato 
e deve cambiare comportamento durante l'esecuzione del programma in base al suo stato

Le operazioni contengono statement condizionali grandi che dipendono dallo stato dell'oggetto.
Lo stato dell'oggetto può essere rappresentanto da una o più constanti numerate.
Il pattern State inserisce ciascun caso dello statement condizionale in una classe separata


Ciò consente di trattare lo stato dell'oggetto  come un vero e proprio oggetto che può cambiare indipendentemente dagli altri oggetti


State è simile a Proxy però a differenza di Proxy utilizza più implementazioni ed un metodo per passare da un implementazione all'altra durante
la vita del surrogato


"""

import collections
from tkinter import ACTIVE


class State_d:
    def __init__(self,imp):
        self.__implementation = imp
        
    def changeImp(self, newImpl):
        self.__implementation = newImpl
        
    def __getattr__(self, name):
        return getattr(self.__implementation,name)

class Implementation1:
    
    def f(self):
        print("Fiddle de dum, Fiddle de dee,")
    
    def g(self):
        print("Eric the half a bee.")
        
    def h(self):
        print("Ho ho ho, tee hee hee,")
    
class Implementation2:
        
    def f(self):
            print("We're Kinght of the Round Table")
        
    def g(self):
            print("We dance whene' er we're able")
        
    def h(self):
            print("We do routines and chorus scene")
            
def run(b):
    b.f()
    b.g()
    b.h()
    b.g()
        
b = State_d(Implementation1())
run(b)
    
b.changeImp(Implementation2())
run(b)
         