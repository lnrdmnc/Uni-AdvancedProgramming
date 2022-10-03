"""
Scrivere uno script in cui vengono importati alcuni moduli
tra quelli forniti da Python e in cui poi viene effettuata la ricerca di una certa funzione a vostra scelta. 
Lo script non deve lanciare eccezioni e non ne deve catturare." 

"""


import sys
import math

#in dir sys ci sta tutto il name space
for arg in dir(sys):
    if(arg=="getsizeof"):
        print("Ho trovato la funzione:",arg)

    


#nome funzione: oggetto
for arg in vars(math):
    pass
