""""


Scriva nel file esercizio4.py un decorator factory decFact(*pos_args,**keyw_args) che
restituisce un decoratore di classe che fa in modo che le istanze della classe vengano
inizializzate come descritto di seguito
• per ogni i =1,..., len(pos_args), vi sia una variabile di istanza con nome uguale a
quello della i-esima stringa di pos_args e valore uguale a None (si assuma che gli
elementi di pos_args siano di tipo str)
• per ogni parametro keyword, vi sia una variabile di istanza con nome e valore
uguali alla chiave e al valore dell’argomento keyword, rispettivamente.
• le inizializzazioni fatte dal metodo __init__ della classe originaria devono
essere preservate e nel caso in cui il metodo __init__ della classe originaria
aggiunga una variabile di istanza con lo stesso nome delle variabili descritte nei
due punti precedenti, allora il valore della variabile deve essere quello
assegnato dal metodo __init__ della classe originaria.

"""

from mimetypes import init

def decFact(*args,**kwargs):

    def decorator(aClass):
        def __init__(self):
            super(aClass,self).__init__()

            for i in range(1, len([*args])):
                if hasattr(self, [*args][i]):
                    pass
                setattr(self,[*args][i],None)
            for j in [*kwargs]:
                if hasattr(self,j):
                    pass
                setattr(self,j,kwargs[j])
            setattr(aClass,"__init__",init)
            return aClass
        return decorator
    
    
    @decFact("wow","oooooooooo",x=100,y=30)
    class aClass:
        pass

    c=aClass()
    print(c.__dict__)