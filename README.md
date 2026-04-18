# Agno Demo

Demo minimale di un agente costruito con Agno che:

- recupera le top story di Hacker News
- classifica ogni titolo in una categoria tecnica
- approfondisce il tema principale della prima notizia tramite Wikipedia
- produce un breve bollettino tech in italiano

Il progetto serve come esempio compatto di orchestrazione di tool esterni con memoria locale persistente tramite SQLite.

## Cosa fa

Il file principale [`agno_demo_hn.py`](./agno_demo_hn.py) definisce un agente con:

- modello `MistralChat("mistral-small-latest")`
- tool di Agno per Hacker News
- tool di Agno per Wikipedia
- una funzione custom `classify_topic()` per classificare i titoli
- database SQLite locale in `tmp/agno_demo.db`

Alla fine dello script viene eseguita una richiesta che:

1. recupera le prime 3 notizie da Hacker News
2. assegna una categoria a ciascun titolo
3. cerca su Wikipedia il tema della prima notizia
4. genera un riepilogo finale in italiano

## Struttura del repository

```text
.
├── agno_demo_hn.py
├── requirements.txt
└── README.md
```

## Requisiti

- Python 3.10+ consigliato
- una chiave API per Mistral
- accesso a Internet durante l'esecuzione, perché lo script usa servizi esterni

Nota: la variabile d'ambiente non è documentata nel repository, ma per l'uso standard del modello Mistral con Agno è tipicamente `MISTRAL_API_KEY`.

## Installazione

Crea un ambiente virtuale e installa le dipendenze:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Imposta poi la chiave API:

```bash
export MISTRAL_API_KEY="la_tua_chiave_api"
```

## Esecuzione

Avvia lo script con:

```bash
python agno_demo_hn.py
```

Se la cartella `tmp/` non esiste, creala prima:

```bash
mkdir -p tmp
```

## Dipendenze

Le dipendenze dichiarate in [`requirements.txt`](./requirements.txt) sono:

- `agno[mistral,sqlite]`
- `ddgs`
- `wikipedia`

## Logica di classificazione

La funzione `classify_topic(title: str) -> str` assegna ogni titolo a una delle seguenti categorie:

- `ai`
- `web`
- `security`
- `business`
- `hardware`
- `other`

La classificazione usa un semplice matching di parole chiave nel titolo. E adatta a una demo, ma resta limitata rispetto a un classificatore semantico.

## Output atteso

L'output viene stampato in streaming sul terminale in formato Markdown. In pratica include:

- elenco delle top story recuperate
- categoria assegnata a ciascun titolo
- breve approfondimento sul tema principale tramite Wikipedia
- sintesi finale in italiano

## Limiti attuali

- lo script è monolitico e non parametrico
- il prompt è hardcoded nel file Python
- la classificazione è basata solo su keyword
- non sono presenti test automatici
- non c'è gestione esplicita degli errori per API key mancanti o problemi di rete

## Possibili estensioni

- rendere configurabile il numero di news da analizzare
- aggiungere una CLI con argomenti
- salvare il report finale su file
- migliorare la classificazione con embedding o LLM routing
- aggiungere test per `classify_topic()`

## Licenza

Nel repository non è presente un file di licenza. Se il progetto deve essere condiviso o riutilizzato, conviene aggiungerne una esplicita.
