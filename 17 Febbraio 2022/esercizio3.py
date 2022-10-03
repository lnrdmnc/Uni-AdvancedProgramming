"""
Scrivere nel file esercizio3.py una classe C per cui accade che ogni volta che si aggiunge una
variabile di istanza ad una delle istanze di C in realta` la variabile viene aggiunta alla classe
come variabile di classe.
Versione con Bonus: modificare il codice in modo tale che le istanze abbiano al piu` due
variabili di istanza: varA e varB (non viene creato __dict__) e non deve essere possibile
aggiungere altre variabili di istanza oltre a queste due. Se il programma avesse bisogno di
aggiungere altre variabili oltre a quelle sopra indicate, queste altre variabili verrebbero create
come variabili di classe e non di istanza

"""
class CiDaproteggere:

    def leggi(self):
        print("leggi")
    
    def scriviA(self):
        print("ScriviA")

    def scriviZ(self):
        print("scriviZ")
    
    def notCallable(self):
        pass

class ProteggiClasse():

    def __init__(self):
        self.implementation= CiDaproteggere()  

    def __getattr__(self,name):

        if name == "notCallable":
            raise AttributeError("Not Allowed")
        return getattr(self.implementation,name)

proteggi= ProteggiClasse()
proteggi.scriviZ()
proteggi.notCallable()  
