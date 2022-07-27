""" 

Scriva nel file esercizio2.py una coroutine find(w,c) che prende in input un carattere c e
una coroutine w e si comporta come segue: ogni volta che riceve un testo, cerca al suo
interno le stringhe che cominciano con c e le invia a w.
Scriva inoltre una coroutine write(file_name) che ogni volta che riceve una stringa la
inserisce nel file di nome file_name seguita da uno spazio. Il parametro w di find e` una
coroutine write.
Suggerimento: potreste usare re.findall(r'\w+', testo) per estrarre le parole da testo.

"""

from fileinput import filename
import re


def coroutine(function):

    def wrapper(*args,**kwargs):
        generator =function(*args,**kwargs)
        next(generator)
        return generator
    return wrapper


@coroutine
def find(c, w):
    while True:
        text=(yield)
        if text:
            lines= re.findall(r'\w+',text)
            print(lines)
            for match in lines:    
                if text.startswith(c):
                    w.send(match)
                    

@coroutine
def write(filename):
    with open(filename,"w") as f:
        while True:
            text=(yield) 
            f.write(text+" ")
        

if __name__=="__main__":
    filename='17 Febbraio 2022\prova.txt'
    w=find('c',write(filename))
    w.send("ciao")
    w.send("ciaocicicipS")


