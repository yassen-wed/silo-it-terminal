# 📟 The Silo IT Terminal (v1.0)

> *"We do not know why we are here. We do not know who built the Silo. We only know the Pact, and the terminal keeps the Pact."*

The **Silo IT Terminal** is an interactive, immersive Slack bot inspired by Hugh Howey's *Wool* trilogy and the sci-fi television adaptation *Silo*. Operating deep within the subterranean infrastructure ("The Deep Down") of your workspace, this system serves as an ancient, heavily monitored mainframe that handles sub-level diagnostics, logs security clearance authentication, and strictly monitors conversational data to enforce the rules of the Pact.

---

## 🛠️ System Features

### 1. Isolated Socket Protocol (Socket Mode)
Mirroring the completely offline, isolated network architecture of the Silo, this bot utilizes the Python `slack-bolt` framework's **Socket Mode Handler**. Instead of exposing public HTTP endpoints, it establishes a persistent, secure WebSocket connection directly with Slack's servers.

### 2. Sub-Level Mechanical Diagnostics (`@bot status`)
Any citizen can query the mainframe to view an instant system readout. It displays critical infrastructural metrics including:
* Structural load distribution (144 Levels nominal)
* Mechanical Dept steam generator pressure (PSI stability thresholds)
* Axial ventilation fan efficiency
* External sensor lens degradation tracking

### 3. Judicial Infraction Enforcement (`@bot outside`)
The Pact strictly prohibits citizens from expressing a desire to leave, discussing the exterior landscape, or referencing unauthorized cleaning rituals. The terminal dynamically monitors input. Triggering keywords instantly flags the transaction as a **Level 1 Subversive Infraction Warning** and simulates an automated transcript forward to Judicial security monitors.

### 4. Restricted Relic Repository (`@bot scavenge`)
Features a built-in **Role-Based Access Control (RBAC)** layer mapped directly to individual Slack Member IDs:
* **Citizens:** Access denied. Scavenging the deep down without a warrant is logged as unauthorized behavior.
* **Head of IT:** Bypasses Judicial security blocks to locate, classify, and secure forbidden artifacts from the "before-times" (e.g., prehistoric tourist guides, antique coins, and forbidden picture books).

---

## 🏗️ Repository Architecture

The project structure is organized as follows:
```text
slack-bot/
├── .env                 # Local environment secrets (Git-ignored)
├── .gitignore           # Excludes credential keys and local caches from VCS
├── requirements.txt     # Locked dependencies for Python environment
└── bot.py               # Main runtime engine and event listener
