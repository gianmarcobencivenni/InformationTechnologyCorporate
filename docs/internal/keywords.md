# Documentazione Aziendale - Keywords & Concetti

## Indice

1. [Sistemi di Supporto Aziendale](#1-sistemi-di-supporto-aziendale)
   - [BSS (Business Support System)](#11-bss-business-support-system)
2. [Gestione delle Relazioni con i Clienti](#2-gestione-delle-relazioni-con-i-clienti)
   - [CRM (Customer Relationship Management)](#21-crm-customer-relationship-management)
   - [CE (Customer Engagement)](#22-ce-customer-engagement)
3. [Supporto e Gestione Operativa](#3-supporto-e-gestione-operativa)
   - [Ticketing](#31-ticketing)
   - [WFM (Workforce Management)](#32-wfm-workforce-management)
   - [HCM (Human Capital Management)](#33-hcm-human-capital-management)
4. [Gestione Finanziaria](#4-gestione-finanziaria)
   - [APEX, CAPEX, OPEX](#41-apex-capex-opex)
5. [Processi di Acquisto](#5-processi-di-acquisto)
   - [RDA (Richiesta di Acquisto)](#51-rda-richiesta-di-acquisto)

---

## 1. Sistemi di Supporto Aziendale

### 1.1 BSS (Business Support System)
Nel contesto del software aziendale, BSS sta per Business Support System. Si riferisce a una categoria di software che supporta le operazioni di back-office in aziende, specialmente quelle legate a telecomunicazioni, utilities o grandi organizzazioni con infrastrutture IT complesse.

#### Dettagli tecnici:
I **BSS** gestiscono vari aspetti del business, come:

- Gestione dei clienti ([CRM](#21-crm-customer-relationship-management))
- Fatturazione e gestione delle entrate
- Gestione degli ordini e dei contratti
- Supporto alle vendite e al marketing

**Approfondimento Microsoft Dynamics 365**:  
Nell'ecosistema Microsoft, il BSS può essere supportato da moduli di Dynamics 365 come **Customer Service**, **Sales**, **Field Service**, e **Project Operations**, che integrano i processi commerciali e amministrativi con soluzioni CRM avanzate.

**Esempio di Journey (Gestione Ordini)**:
1. Il cliente effettua un ordine tramite il portale aziendale (integrato con Dynamics CRM).
2. L'ordine viene inserito nel sistema BSS per la gestione.
3. Il sistema invia una notifica all'ufficio acquisti e ai reparti di fatturazione.
4. L'ordine viene monitorato attraverso Power Automate per l'invio al cliente.

---

## 2. Gestione delle Relazioni con i Clienti

### 2.1 CRM (Customer Relationship Management)
Il Customer Relationship Management (CRM) è una strategia che si focalizza sulla gestione delle interazioni con i clienti per migliorare il servizio, incrementare la fidelizzazione e supportare la crescita delle vendite.

#### Dettagli tecnici:
Microsoft Dynamics 365 CRM consente di centralizzare tutte le informazioni sui clienti e offre strumenti per ottimizzare le interazioni in modo personalizzato.

**Approfondimento Microsoft Dynamics 365**:  
Il modulo **Sales** di Dynamics 365 è uno dei principali strumenti CRM, che aiuta a gestire le pipeline di vendita, i lead e i contratti, integrato con **Power BI** per l'analisi dei dati e **Power Automate** per automatizzare i processi di follow-up.

**Esempio di Flow (Lead Management)**:
1. Un lead viene generato tramite una campagna marketing.
2. Il sistema CRM crea automaticamente una scheda cliente.
3. Un task viene assegnato a un venditore per il follow-up.
4. Se l'interazione va a buon fine, il lead si trasforma in opportunità di vendita.

### 2.2 CE (Customer Engagement)
Il Customer Engagement si focalizza sul coinvolgimento attivo dei clienti con l'azienda su vari canali (digitali e fisici).

#### Dettagli tecnici:
CE è strettamente integrato con i moduli **Dynamics 365 Marketing** e **Customer Service**, consentendo di pianificare campagne, interazioni personalizzate e migliorare l'engagement in base ai dati raccolti dai clienti.

**Approfondimento Microsoft Dynamics 365**:  
Dynamics 365 **Marketing** utilizza il concetto di customer journey per creare esperienze personalizzate attraverso vari canali di comunicazione (email, social media, SMS).

**Esempio di Journey (Campagna di Email Marketing)**:
1. Un cliente partecipa a un evento organizzato dall'azienda.
2. Il sistema invia un'email di ringraziamento con un'offerta personalizzata.
3. Se il cliente interagisce, un workflow automatizzato crea un task per il venditore per contattarlo direttamente.

---

## 3. Supporto e Gestione Operativa

### 3.1 Ticketing
Il ticketing è un sistema di gestione delle richieste dei clienti, integrato nei sistemi CRM per mantenere traccia delle interazioni e risolvere problemi o richieste.

#### Dettagli tecnici:
Il modulo **Customer Service** di Dynamics 365 supporta il ticketing, con funzioni integrate di routing automatico dei ticket, gestione dei livelli di priorità e tracking delle risoluzioni tramite **Power Automate**.

**Esempio di Flow (Gestione Ticket)**:
1. Il cliente invia una richiesta di supporto tramite il portale aziendale (integrato con Dynamics CRM).
2. Un ticket viene generato automaticamente e assegnato al team di supporto.
3. Il ticket viene risolto e chiuso, inviando una notifica automatica al cliente.

### 3.2 WFM (Workforce Management)
Il Workforce Management si riferisce alla gestione e ottimizzazione delle risorse umane, con particolare attenzione alla pianificazione, assegnazione dei compiti e monitoraggio delle prestazioni.

#### Dettagli tecnici:
In un contesto Microsoft Dynamics, il WFM può essere implementato utilizzando **Dynamics 365 Field Service**, che permette la gestione delle squadre sul campo, ottimizzando la loro pianificazione e le risorse tramite integrazione con **Power BI** e **Power Automate**.

**Esempio di Flow (Pianificazione delle Risorse)**:
1. Un ticket di assistenza richiede l'intervento di un tecnico sul campo.
2. Il sistema Field Service ottimizza la pianificazione in base alla disponibilità delle risorse.
3. Il tecnico completa l'intervento, chiude il ticket e il CRM aggiorna automaticamente lo stato.

### 3.3 HCM (Human Capital Management)
L'Human Capital Management (HCM) si riferisce a una serie di pratiche e software progettati per gestire le risorse umane di un'organizzazione, ottimizzando la gestione del personale e migliorando le prestazioni lavorative.

#### Funzioni principali del software HCM:
1. **Recruitment**: Gestione del processo di assunzione, dalla pubblicazione degli annunci di lavoro alla selezione e all'assunzione di candidati.
2. **Onboarding**: Integrazione dei nuovi dipendenti nell'organizzazione, facilitando la formazione e l'adattamento.
3. **Gestione delle performance**: Monitoraggio e valutazione delle prestazioni dei dipendenti, inclusi obiettivi, feedback e piani di sviluppo.
4. **Formazione e sviluppo**: Programmi di formazione per migliorare le competenze e le conoscenze dei dipendenti, promuovendo la crescita professionale.
5. **Gestione delle retribuzioni**: Elaborazione dei salari, gestione delle buste paga e calcolo delle tasse e dei contributi.
6. **Gestione delle competenze**: Identificazione delle competenze necessarie per i ruoli aziendali e monitoraggio delle competenze dei dipendenti.
7. **Analisi dei dati HR**: Raccolta e analisi di dati relativi al personale per prendere decisioni informate e migliorare le pratiche di gestione delle risorse umane.

#### Approfondimento Microsoft Dynamics 365:
Dynamics 365 offre un modulo **Human Resources** che consente di gestire e ottimizzare le pratiche HCM, integrando funzioni di onboarding, gestione delle performance e analisi dei dati.

#### Esempi di software HCM:
Alcuni software HCM comuni includono:
- **SAP SuccessFactors**
- **Workday**
- **Oracle HCM Cloud**
- **ADP Workforce Now**
- **BambooHR**

---

## 4. Gestione Finanziaria

### 4.1 APEX, CAPEX, OPEX
APEX, CAPEX e OPEX sono termini utilizzati per descrivere differenti tipi di spese in ambito aziendale.

#### Dettagli tecnici:
- **CAPEX** (Capital Expenditure): Spese in conto capitale, come l'acquisto di beni fisici o software aziendali.
- **OPEX** (Operational Expenditure): Spese operative, come salari, utenze e manutenzione.
- **APEX**: Termini finanziari meno comuni, possono riferirsi a metriche di performance o scambi annualizzati.

**Approfondimento Microsoft Dynamics 365**:  
Le funzionalità di **Dynamics 365 Finance** e **Project Operations** permettono di gestire e tracciare CAPEX e OPEX in tempo reale, integrando le informazioni con moduli CRM per un'ottimizzazione delle risorse.

**Esempio di Flow (Gestione Spese)**:
1. Un nuovo progetto richiede un investimento significativo (CAPEX).
2. Le spese vengono tracciate e approvate tramite Dynamics 365 Finance.
3. Le operazioni quotidiane (OPEX) vengono monitorate tramite Power BI per un controllo continuo dei costi.

---

## 5. Processi di Acquisto

### 5.1 RDA (Richiesta di Acquisto)
La Richiesta di Acquisto (RDA) formalizza la necessità di acquistare beni o servizi all'interno di un'organizzazione.

#### Dettagli tecnici:
Dynamics 365 **Supply Chain Management** integra il processo di RDA con la gestione degli acquisti, consentendo flussi di approvazione automatizzati tramite **Power Automate** e monitoraggio delle spese tramite **Dynamics 365 Finance**.

**Esempio di Flow (Processo RDA)**:
1. Un dipendente inoltra una RDA tramite il portale aziendale.
2. La richiesta viene approvata automaticamente tramite Power Automate se rispetta determinate soglie di spesa.
3. L'ordine di acquisto viene generato e tracciato tramite Dynamics 365 Supply Chain Management.

