# Esperimenti di Machine Learning con Google Analytics

## 1 Test

Il primo test consiste nel far imparare le statistiche del mio sito degli ultimi 3 anni ed estrapolare dallo slug i termini. 
Con un pulizia, manuale ed una automatica si ottengono da 474 voci se ne ottengono 481. 

Dando:
```
./cleaner.py & analytics.py
```

Si ottiene un underfitting che significa che il materiale di addestramento è troppo poco per permettergli di imparare e quindi non riesce ad indovinare.

le motivazioni sono due:

* I dati non sono coerenti nel tempo ()ovvero un periodo altri termini portavano più traffico)
* I 665 termini utilizzati non sono sufficenti per permettergli di imparare

## 2 Test

Dall'esperienza del primo test si è dimostrato che i dati non sono sufficenti quindi il prossimo passo è fornirgliene di più. 

L'idea è di estrapolare il contenuto di tutti questi articoli e fornirgli quello come materiale da imparare invece dei termini dello slug. 
Quindi con uno scraper che utilizza le WP Rest API si scaricherà tutto il testo che verrà poi pulito per togliere tutte le parole non necessarie come congiunzioni o articoli. 

Dopodiche si sostituirà nel CSV il contenuto pulito invece di degli slug facendo fare delle comparazioni sempre con le visite e gli accessi.

# Scopo

Riuscire a creare un modello che dato un termine riesca a fornire quanto successo in termini di visite e accessi può portare al sito.