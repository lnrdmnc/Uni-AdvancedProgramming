import copy

def outer_function(msg):
    message= msg
    
    def inner_function():
        print(message)
    return inner_function

hy_func = outer_function('hi')
bye_func = outer_function('bye')

hy_func()
bye_func()


"""

Scrivere nel file esercizio2.py un decoratore di classe decoraClasse che aggiunge alla classe 
decorata il metodo conQualiArgomenti che restituisce una tupla contenente 
• i valori di tutti gli argomenti posizionali (compresi quelli variabili) 
• le coppie (chiave, valore) di tutti gli argomenti keyword (compresi quelli variabili) 
passati all’ultima invocazione di __init__ .

"""

def decoraClasse(cls):
    
    oldInit = cls.__init__
    
    def __newinit__(self,*args,**kwargs):
        if(cls == type(self)):
            cls.args= copy.deepcopy(args)
            cls.kwargs = copy.deepcopy(kwargs)


    def conQualiArgomenti(self):
        return (cls.args, cls.kwargs)
    
    
    cls.__init__ = __newinit__
    cls.conQualiArgomenti = conQualiArgomenti
    return cls

@decoraClasse
class Classe:
    
    def __init__(self,*args,**kwargs):
        print(args)
        print(kwargs)
        
if __name__ == '__main__':
    x= Classe(1,2,3)
    x= Classe(1,2,4, kwarg1=3, kwarg2=6)
    print(x.conQualiArgomenti())