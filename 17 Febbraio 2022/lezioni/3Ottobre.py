class myClass:
    #metodo istanza
    def call(self,*args,**kwargs):
        pass


#Overrirding riguarda un sacco di funzioni built in quindi possiamo sovrascriverli per personalizzarl, ricordiamo che non esistono metodi di default
#tutto ciò che sta nelle sottoclassi oscura ciò che è nelle superclassi 


#il metodo __iter__ restituisce un iteratore per un oggetto contenitore
#il for invoca l'iteratore e crea una variabile temporanea senza nome per immagazzinare l'iteratore durante il loop
#non serve per forza implementare iter infatti se ci sta len e getitem  allo stesso tempo ci sta anche iter 
#se iter è presente allora è presente anche contains 


#Eriditarietà sopra sotto sinistra destra 
#vedere mro per sovrascrivere __mro__ ci vuole una metaclasse


class A:
    pass
class B:
    pass
class C:
    pass

class D(A,B,C):
    pass

print(D.__mro__)

#posso agire sulle classi base __bases__ andando a modificare l'ordine delle classi base 
#non ho capito si può fare anche con mro


class A:
    pass
class C(A):
    pass

C.__bases__=(A,)

