# Agno Agentic Demo

Questo repository mostra una piccola applicazione di Agentic AI costruita con **Agno**.
L'agente non si limita a generare testo: riceve un obiettivo, usa tool esterni, mantiene contesto operativo e compone un risultato finale attraverso piu passaggi.

In questa demo il workflow agentico parte da Hacker News, interpreta le notizie, le classifica, approfondisce il tema principale con Wikipedia e genera un bollettino tech in italiano.

## Perche e un'applicazione agentica

Il progetto mette in evidenza alcuni elementi centrali di un **agentic workflow**:

- **goal-oriented execution**: l'agente riceve un task composito e lo porta a termine orchestrando piu azioni
- **tool use**: usa sorgenti esterne durante il processo, non solo conoscenza interna del modello
- **multi-step reasoning**: combina raccolta dati, classificazione, approfondimento e sintesi finale
- **memory and context**: usa storico e persistenza locale per mantenere continuita di esecuzione
- **final synthesis**: trasforma dati eterogenei in un output leggibile e coerente

Il punto chiave della demo e proprio questo: mostra come **Agno** consenta di costruire applicazioni in cui il modello agisce come un agente operativo, non come un semplice generatore di testo.

## Workflow dell'agente

Lo script [`agno_demo_hn.py`](./agno_demo_hn.py) definisce un agente che:

1. recupera le top story da Hacker News
2. classifica ogni titolo con una funzione custom
3. approfondisce via Wikipedia il tema della prima notizia
4. sintetizza tutto in un bollettino tech in italiano

Questo flusso rappresenta una pipeline agentica compatta ma concreta, in cui un singolo agente coordina tool, logica applicativa e generazione finale.

## Agno come framework agentico

L'applicazione sfrutta Agno per combinare:

- definizione dell'agente
- istruzioni operative
- uso di tool esterni
- memoria conversazionale
- persistenza locale con SQLite
- output Markdown in streaming

Lo stack attuale comprende:

- `Agent` di Agno come orchestratore del workflow
- `HackerNewsTools` per il recupero delle notizie
- `WikipediaTools` per l'arricchimento contestuale
- `classify_topic()` come tool custom di dominio
- `SqliteDb('tmp/agno_demo.db')` per memoria e storico locale

## Modello LLM intercambiabile

Nel codice corrente il backend configurato e:

```python
MistralChat("mistral-small-latest")
```

Ma il progetto non e legato a Mistral come scelta architetturale.
La vera base dell'applicazione e **Agno** con il suo approccio agentico. Il provider LLM puo essere sostituito in base alle esigenze del caso d'uso.

Lo stesso workflow puo essere adattato anche ad altri modelli o provider, ad esempio:

- OpenAI
- Groq
- Anthropic
- Gemini
- altri backend compatibili supportati da Agno

In pratica: il modello cambia, il workflow agentico resta.

## Cosa dimostra questa demo

Questo repository mostra come costruire un agente capace di:

- usare tool multipli in una singola esecuzione
- arricchire il ragionamento con dati live
- comporre task sequenziali orientati a un obiettivo
- conservare memoria locale
- produrre un output finale pronto per l'utente

E una base efficace per chi vuole iniziare a sviluppare applicazioni di **Agentic AI**, **tool-augmented reasoning** e **LLM orchestration** con Agno.

## Struttura del repository

```text
.
├── agno_demo_hn.py
├── requirements.txt
└── README.md
```

## Requisiti

- Python 3.10+ consigliato
- accesso a Internet durante l'esecuzione
- una chiave API per il provider LLM scelto

Nel codice attuale e usato Mistral, quindi serve tipicamente:

```bash
export MISTRAL_API_KEY="la_tua_chiave_api"
```

Se sostituisci il modello con un altro backend Agno, dovrai configurare la relativa API key.

## Installazione

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdir -p tmp
```

## Esecuzione

```bash
python agno_demo_hn.py
```

All'avvio, l'agente esegue direttamente il workflow completo e stampa il risultato in streaming sul terminale.

## Dipendenze

Le dipendenze dichiarate in [`requirements.txt`](./requirements.txt) sono:

- `agno[mistral,sqlite]`
- `ddgs`
- `wikipedia`

## Evoluzioni possibili

Questa base puo essere estesa verso applicazioni agentiche piu ricche, ad esempio:

- newsletter tech generate automaticamente
- agenti di monitoraggio news per domini specifici
- research assistant con piu tool
- workflow multi-step piu articolati
- architetture multi-agent

## Licenza

Questo progetto e distribuito sotto licenza [MIT](./LICENSE).
