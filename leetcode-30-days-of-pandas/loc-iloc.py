import pandas as pd
"""
Questo script mostra diversi esempi di utilizzo di `.loc` in pandas per selezionare dati da un DataFrame.
`loc` è un metodo di pandas che permette di accedere a un gruppo di righe e colonne per etichetta o array booleano. 
Si usa principalmente per selezionare dati in base ai nomi degli indici e delle colonne, piuttosto che alle loro posizioni numeriche.
Esempi inclusi nel codice:
- Selezione di righe specifiche tramite le etichette degli indici.
- Selezione di righe e colonne specifiche tramite le etichette.
- Selezione condizionale di righe (ad esempio, tutte le persone con età maggiore di 25 anni) e di colonne specifiche.
Sintassi generale:
    df.loc[righe, colonne]
Dove:
- `righe` può essere una singola etichetta, una lista di etichette o una condizione booleana.
- `colonne` può essere una singola etichetta o una lista di etichette di colonne.
Nota: `.loc` include sia l'indice iniziale che quello finale quando si usa uno slicing con etichette.
"""

df = pd.DataFrame({
    'nome': ['Anna', 'Luca', 'Marco', 'Sara'], 
    'età': [25, 30, 22, 28], 
    'città': ['Roma', 'Milano', 'Torino', 'Napoli']
}, index=['a', 'b', 'c', 'd'])

#print(df) # al posto degli indici numerici ci sono a, b, c, d

#print(df.loc[['b', 'c']])

#print(df.loc[['a', 'd'], ['nome', 'età']])

print(df.loc[df['età']> 25, ['nome', 'città']])