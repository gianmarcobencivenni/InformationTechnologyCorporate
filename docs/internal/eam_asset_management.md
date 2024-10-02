# EAM (Enterprise Asset Management)

## Indice
1. [Struttura gerarchica inventario](#1-struttura-gerarchica-inventario)
    - [Entità](#11-entità)
    - [Gerarchia](#11-entità)
---

## 1. Struttura gerarchica inventario

### 1.1 Entità
Esistono 2 tipologie di entità:
- Posizioni Funzionali
- Oggetti : fanno parte dei livelli 3, 4 e 5 della gerarchia dell'inventario, ereditano il tipo dalla posizione funzionale soprastante

### 1.2 Gerarchia
**Gerarchia a 5 Livelli** (implementata l'ereditarietà)
- IMPIANTO (**livello 1**, posizione funzionale a singola istanza)
    - SISTEMA (**livello 2**, posizione funzionale a singola istanza, *is a kind of* IMPIANTO)
        - COMPONENTE (**livello 3**, oggetto, *is a kind of* SISTEMA)
            - MODULO (**livello 4**, oggetto, *is a kind of* COMPONENTE)
                - ELEMENTO (**livello 5**, oggetto, *is a kind of* MODULO)