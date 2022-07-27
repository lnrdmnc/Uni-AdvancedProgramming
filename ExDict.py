"""  Eserciizo 1 sui dizionari 

Il primo esercizio ci consente di di prendere delle liste ed elaborarle al fine di creare una lista di dizionari

Creare tre liste che rappresentano tre elenchi di nomi, cognomi ed età.
Ad esempio nomi: Tom,Mario,Luisa;
cognomi: Rossi, Verdi, Gialli 
Creare una nuova lista dove ogni elemento è rappresentanto del tipo da {'nome':nome, 'cognome': cognome, 'età':età}
Gli elementi dovranno essere accoppiati in base all'ordine

"""

names =['Tom','Mario', 'Luisa']
surnames= ['Rossi','Verdi','Gialli']
ages= [22,21,23]

contacts = []

for name, surname, age in zip(names,surnames,ages):
    contacts.append({'nome': name,'cognome': surname,'età': age})
print (contacts)


""" Creare un dict che contiene nomi cognome matricola e nel caso inserire un esame il nome e il voto """


contacts = {'name':'Tom', 'surname':'Verdi'}

contacts ['matricola'] = input('Inserisci il numero della matricola: ')
contacts ['esami'] = []

n = int(input('Quante materie aggiungere'))

for i in range (1, n + 1):
    
    materia = input('Inserisci la materia')
    voto = int (input('Inserisci il voto'))
    contacts ['esami'] += [{'materia': materia, 'voto': voto}]

print(contacts)


 
