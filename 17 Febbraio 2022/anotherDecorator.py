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



"""

Scriva nel file esercizio1.py una classe StranaTupla che estende la classe tuple e funziona in
modo tale che ogni volta che viene creata una sua istanza questa contiene solo gli elementi
di ordine dispari della collezione iterabile passata a StranaTupla(). Ad esempio, se viene
invocato StranaTupla([‘a’,’h’,5,’dado’,4]) allora l’istanza di StranaTupla creata è (‘a’, 5,4).

"""




class StranaTupla(tuple):

    def __new__(self,*args):
        l=list()
        for i,x in enumerate(args):
            if(i%2==0):
                l.append(args[i])
        return tuple(l)



strana = StranaTupla('a','h',5,'dado',4)
print(strana)

    
"""
Scrivere il decoratore di funzione decora che trasforma la funzione 
decorata in una funzione che lancia l’eccezione TypeError se uno o 
più argomenti non sono di tipo str. La funzione deve restituire una 
stringa formata dagli argomenti ricevuti in input e dal risultato 
intervallati da uno spazio. Non dimenticate di convertire il risultato in 
stringa quando lo inserite nella stringa output

"""   

def decoratore(fun):
    def wrapper(*args,**kwargs):
        name="_"
        for i,arg in enumerate(args):
            if(arg==type(str)):
                name=arg+"_"
                return name
            else: TypeError("ddd")
    return wrapper

@decoratore
def fun(*args,**kwargs):
    return sum(args)

print(fun("ciao",1))