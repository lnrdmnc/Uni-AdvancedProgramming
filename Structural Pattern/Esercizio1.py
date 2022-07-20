
""""
Scrivere il decoratore di funzione decf che fa in modo che venga
lanciata l ’eccezione TypeError se il numero di argomenti è diverso da
due. Altrimenti, se la funzione decorata restituisce un risultato,
questo viene aggiunto insieme al valore del primo argomento in un
file di nome “risultato.txt”.
• Suggerimento: Ricordatevi di convertire a stringa il valore del primo
argomento e il risultato quando li scrivete nel file e di aprire il file in
modo da non cancellare quanto scritto precedentemente nel file.
"""""

def decf(f):
    @wrap(f)
    def wrapper(*args,**kwargs):
        if len(args)+ len(kwargs)!=2:
            raise TypeError
        else:
            f_o=open("risultato.txt",'a')
            res=f(*args,**kwargs)
            if res!=None:
                f_o.write(res)
            if args:
                f_o.write(str(args[0]))
            else:
                f_o.write(str(next(iter(kwargs.values()))))
            f_o.write("\n")
            f_o.close()
        return wrapper

