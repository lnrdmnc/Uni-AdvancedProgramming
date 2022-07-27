"""
Scriva nel file esercizio1.py una classe StranaTupla che estende la classe tuple e funziona in
modo tale che ogni volta che viene creata una sua istanza questa contiene solo gli elementi
di ordine dispari della collezione iterabile passata a StranaTupla(). Ad esempio, se viene
invocato StranaTupla([‘a’,’h’,5,’dado’,4]) allora l’istanza di StranaTupla creata è (‘a’, 5,4

"""

class StranaTupla(tuple):
    def __new__(cls,*args,**kwargs):

        n_list=list()
        for i in range(0, len([*args,*kwargs])):
            if i %2==0:
                n_list.append([*args,*kwargs][i])
        return tuple(n_list)

strana= StranaTupla('a','h',5,'dado',4)
print(strana)


"""output 'a', '5, '4' """