# Guida Introduttiva a VBScript

## Cos'è VBScript?

**VBScript (Visual Basic Scripting Edition)** è un linguaggio di scripting sviluppato da Microsoft. Deriva da Visual Basic ed è pensato per essere un linguaggio leggero e facile da utilizzare per l'automazione di attività su piattaforme Windows.

### Caratteristiche Principali:

- **Interpretato**: VBScript è un linguaggio interpretato, il che significa che non richiede compilazione. Gli script vengono eseguiti dall'interprete integrato nel sistema operativo Windows.
- **Semplicità**: Ha una sintassi semplice e facile da apprendere, soprattutto per chi ha familiarità con Visual Basic.
- **Integrazione con Windows**: Può interagire direttamente con il sistema operativo Windows e con le applicazioni COM (Component Object Model).
- **Utilizzo in Pagine Web**: In passato, VBScript era utilizzato per scripting lato client nelle pagine web all'interno di Internet Explorer. Tuttavia, questo uso è ormai obsoleto e non supportato nei browser moderni.

## Tipologia di Linguaggio

### Paradigma di Programmazione

VBScript è principalmente un linguaggio di scripting **procedurale**. Non supporta la programmazione orientata agli oggetti (OOP) nel senso completo del termine, ma permette l'uso di **oggetti** tramite l'automazione COM.

### Oggetti e COM

- **Creazione di Oggetti COM**: VBScript può creare e manipolare oggetti COM utilizzando la funzione `CreateObject`. Questo permette di interagire con una vasta gamma di applicazioni e componenti di Windows, come Excel, Word, o componenti di sistema.
  
```vbscript
Set objFSO = CreateObject("Scripting.FileSystemObject")
```

**Limitazioni OOP**: Non è possibile definire classi personalizzate, ereditarietà o polimorfismo come nei linguaggi orientati agli oggetti completi.

## Utilizzo in Ambito Aziendale
VBScript è ampiamente utilizzato nelle aziende per automatizzare attività amministrative e di gestione su sistemi Windows. Ecco alcuni esempi:

- **Automazione di Office**: Interagire con applicazioni Microsoft Office come Excel, Word o Outlook per elaborare documenti, inviare email, generare report.

- **Gestione di Sistema**: Script per gestire utenti, gruppi, permessi, installazione di software, backup, manipolazione del registro di sistema.

- **Manipolazione di File e Cartelle**: Utilizzo del FileSystemObject per copiare, spostare, eliminare file e cartelle.

- **Login Scripts**: Esecuzione di script all'accesso dell'utente per configurare l'ambiente di lavoro.

- **Monitoraggio e Reportistica**: Raccolta di informazioni di sistema, monitoraggio di servizi, generazione di log.

## Sintassi e Keywords Principali
### Variabili
Le variabili in VBScript sono debolmente tipizzate e non richiedono dichiarazione del tipo.
```vbscript
Dim nome
nome = "Mario Rossi"
```

### Costanti
```vbscript

Const PI = 3.1416
```

### Strutture di Controllo
- If...Then...Else
```vbscript
If condizione Then
    ' Codice se la condizione è vera
Else
    ' Codice se la condizione è falsa
End If
```

- Select Case
```vbscript
Select Case espressione
    Case valore1
        ' Codice
    Case valore2
        ' Codice
    Case Else
        ' Codice
End Select
```


- For...Next
```vbscript
For i = 1 To 10
    ' Codice
Next
```


- For Each...Next
```vbscript
For Each elemento In collezione
    ' Codice
Next
```


- Do While / Do Until
```vbscript
Do While condizione
    ' Codice
Loop
```

### Funzioni e Subroutine
In VBScript, funzioni e subroutine sono entrambe utilizzate per organizzare e riutilizzare il codice, ma ci sono alcune differenze chiave tra i due:
- Funzione: Una funzione è progettata per restituire un valore. Puoi utilizzare l'istruzione Function per definirla e l'istruzione FunctionName = valore per restituire il valore.
```vbscript
Function NomeFunzione(parametri)
    ' Codice
    NomeFunzione = risultato
End Function
```

- Subroutine: Una subroutine, definita con Sub, non restituisce alcun valore. Viene utilizzata principalmente per eseguire un blocco di codice senza restituire un risultato.
```vbscript
Sub NomeSubroutine(parametri)
    ' Codice
End Sub
```

- Esempio pratico:
```vbscript
Function Somma(a, b)
    Somma = a + b  ' Restituisce la somma
End Function

Sub StampaMessaggio()
    WScript.Echo "Questo è un messaggio dalla subroutine"
End Sub

' Utilizzo delle funzioni e subroutine
Dim risultato
risultato = Somma(5, 10)  ' Chiamata alla funzione
WScript.Echo "Risultato della somma: " & risultato

StampaMessaggio()  ' Chiamata alla subroutine
```

### Error Handling
In VBScript, la gestione degli errori non segue la stessa sintassi del costrutto try...except presente in linguaggi come Python o Java. Tuttavia, VBScript fornisce alcune istruzioni per gestire gli errori in modo efficace. Ecco come funziona:


- **On Error Resume Next**: Questa istruzione consente di ignorare gli errori e di continuare l'esecuzione del codice. Quando si utilizza questa istruzione, se si verifica un errore, il controllo passa all'istruzione successiva.

```vbscript

On Error Resume Next
' Codice che potrebbe generare un errore
Dim x
x = 1 / 0  ' Divisione per zero

If Err.Number <> 0 Then
    WScript.Echo "Si è verificato un errore: " & Err.Description
End If

' Reset dell'oggetto Err
Err.Clear
```

- On Error GoTo: Questo approccio permette di reindirizzare il flusso di esecuzione a una parte specifica del codice in caso di errore. È simile al try...catch in altri linguaggi.

```vbscript
On Error GoTo ErrorHandler

' Codice che potrebbe generare un errore
Dim y
y = 1 / 0  ' Divisione per zero

Exit Sub  ' Esce dalla subroutine prima dell'handler

ErrorHandler:
    WScript.Echo "Si è verificato un errore: " & Err.Description
    Err.Clear  ' Reset dell'oggetto Err
End Sub
```


### Oggetti Principali
- WScript: Oggetto principale quando si eseguono script tramite Windows Script Host.
```vbscript
WScript.Echo "Messaggio"
```
- FileSystemObject: Per manipolare file e cartelle.
```vbscript
Set fso = CreateObject("Scripting.FileSystemObject")
```
- Dictionary: Struttura dati per memorizzare coppie chiave-valore.
```vbscript
Set dict = CreateObject("Scripting.Dictionary")
dict.Add "chiave", "valore"
```


### Keywords Principali
Ecco un elenco delle parole chiave più comuni in VBScript:

- **Dim**: Dichiara una o più variabili.
- **Set**: Assegna un riferimento a un oggetto.
- **If, Then, Else, ElseIf, End If**: Struttura condizionale.
- **Select Case, Case, End Select**: Struttura di selezione multipla.
- **For, To, Step, Next**: Ciclo con contatore.
- **For Each, In, Next**: Ciclo per iterare attraverso una collezione.
- **Do, While, Until, Loop**: Ciclo basato su una condizione.
- **Function, End Function**: Definisce una funzione che può restituire un valore.
- **Sub, End Sub**: Definisce una subroutine che non restituisce un valore.
- **Call**: Utilizzato per chiamare una subroutine.
- **Const**: Dichiara una costante.
- **On Error Resume Next**: Gestione degli errori.
- **Option Explicit**: Richiede la dichiarazione esplicita di tutte le variabili utilizzando Dim.