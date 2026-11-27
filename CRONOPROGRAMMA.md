# 🗓️ Cronoprogramma e Scadenze

> **Nota:** Questo file riporta la pianificazione macro delle fasi e le milestone principali. Per il dettaglio giornaliero fare riferimento alla vista **Roadmap** su GitHub Projects.

## 🎯 Milestone Principali
| Codice | Milestone | Data Target | Referente | Stato |
| :--- | :--- | :---: | :--- | :---: |
| **MS-01** | Chiusura rilievi e specifiche tecniche iniziali | 2026-12-04 | `@utente1` | 🟢 Raggiunta |
| **MS-02** | Emissione pacchetto elaborati per approvazione | 2026-12-15 | `@utente2` | 🟡 In corso |
| **MS-03** | Validazione definitiva e consegna fascicolo | 2026-12-22 | `@utente1` | ⚪ Pianificata |

---

## 📅 Dettaglio Temporale Fasi (Gantt Tabellare)

| ID | WBS | Attività / Fase | Referente | Data Inizio | Scadenza | Dipendenze | Priorità |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **AT-01** | WP1.1 | Raccolta dati e sopralluogo tecnico | `@utente1` | 2026-12-01 | 2026-12-04 | — | Alta |
| **AT-02** | WP1.2 | Redazione elaborati tecnici e verifiche | `@utente2` | 2026-12-05 | 2026-12-12 | AT-01 | Critica |
| **AT-03** | WP2.1 | Stesura documentazione tecnica e procedure | `@utente3` | 2026-12-08 | 2026-12-15 | AT-01 | Alta |
| **AT-04** | WP1.3 | Revisione interna e controllo qualità | `@utente1` | 2026-12-13 | 2026-12-17 | AT-02, AT-03 | Critica |
| **AT-05** | WP2.2 | Emissione ufficiale e archiviazione | `@utente1` | 2026-12-18 | 2026-12-22 | AT-04 | Media |
