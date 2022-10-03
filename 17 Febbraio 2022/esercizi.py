"""Scrivere una classe di base ClsBase in cui c’e` un metodo addAttr che controlla se la
classe ha l’attributo di nome s e se tale attributo non e` presente allora aggiunge
l’attributo s con valore v; in caso contrario non fa niente. Il metodo deve funzionare
anche per le eventuali sottoclassi agendo sulla sottoclasse senza bisogno pero` di
essere ridefinito nella sottoclasse.

"""


class ClsBase:

    def addAttr(cls):
        privateName={}
        if privateName is not 's':
            privateName='s'


