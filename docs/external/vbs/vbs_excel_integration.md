# Tutorial: Automazione Excel con VBScript

In questo tutorial imparerai come utilizzare **VBScript (VBS)** per aprire, leggere, scrivere e manipolare dati in un file Excel. Questo script può essere utile per automatizzare operazioni su database in formato Excel.

## Prerequisiti

- Sistema operativo Windows.
- Microsoft Excel installato.
- Editor di testo semplice come **Notepad** o **VSCode**.

## 1. Creazione di un File VBScript

Crea un nuovo file con estensione `.vbs` (ad esempio `script_excel.vbs`). Questo sarà il file in cui scriverai il codice VBScript.

## 2. Aprire un File Excel con VBScript

Ecco come aprire un file Excel esistente.

```vbscript
' Creiamo un oggetto Excel
Set objExcel = CreateObject("Excel.Application")

' Nascondiamo l'applicazione Excel (facoltativo)
objExcel.Visible = False

' Apriamo il file Excel specificato
Set objWorkbook = objExcel.Workbooks.Open("C:\percorso\del\file.xlsx")

' Accesso al primo foglio
Set objSheet = objWorkbook.Sheets(1)

' Chiudiamo il file senza salvare (esempio)
objWorkbook.Close False
objExcel.Quit

' Puliamo gli oggetti
Set objSheet = Nothing
Set objWorkbook = Nothing
Set objExcel = Nothing
```

## Spiegazione
- CreateObject("Excel.Application"): crea un'istanza di Excel.
- Visible = False: Excel viene eseguito in background.
- Workbooks.Open: apre un file Excel esistente.
- Sheets(1): accede al primo foglio del workbook.
- Close False: chiude il file senza salvare le modifiche.

## 3. Leggere Dati da Excel
Per leggere i dati da una cella specifica in Excel, utilizza il codice seguente:
```vbscript
' Leggiamo il valore della cella A1 nel primo foglio
Dim valore
valore = objSheet.Cells(1, 1).Value

' Visualizziamo il valore letto
MsgBox "Il valore della cella A1 è: " & valore
```
## Spiegazione
- Cells(1, 1).Value: legge il valore nella cella A1 (riga 1, colonna 1).
- MsgBox: visualizza un messaggio con il valore letto.

## 4. Scrivere Dati su Excel
```vbscript
' Scriviamo un valore nella cella B2
objSheet.Cells(2, 2).Value = "Nuovo Valore"

' Salviamo il workbook
objWorkbook.Save
```
## Spiegazione
- Cells(2, 2).Value = "Nuovo Valore": scrive il valore "Nuovo Valore" nella cella B2 (riga 2, colonna 2).
- objWorkbook.Save: salva le modifiche nel file Excel.


## 5. Chiudere il File Excel e Rilasciare le Risorse
```vbscript
' Chiudiamo il workbook e l'applicazione Excel
objWorkbook.Close True  ' Salviamo e chiudiamo
objExcel.Quit

' Pulizia degli oggetti
Set objSheet = Nothing
Set objWorkbook = Nothing
Set objExcel = Nothing
```
## Spiegazione
- objWorkbook.Close True: chiude il file e salva le modifiche.
- objExcel.Quit: chiude l'applicazione Excel.
- Set ... = Nothing: pulisce gli oggetti per liberare la memoria.