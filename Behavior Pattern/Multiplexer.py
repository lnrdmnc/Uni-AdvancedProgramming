""" 
    Prendiamo come esempio un multiplexer 
    
    ha due stati 
    attivo il mu accetta connessioni, nome evento, callback dove ogni callback è un qualsiasi callable
    dormiente: l'invocazione dei suoi metodi non ha alcun effetto( comportamento safe)
    
"""

class Multiplixer:
    ACTIVE,DORMANT = ("ACTIVE","DORMANT")
    
    def __init__(self):
         self.callbacksForEvent = collections.defaultdict(list)
         self.state = Multiplixer.ACTIVE