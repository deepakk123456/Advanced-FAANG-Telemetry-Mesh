# ☣️ Advanced Microservice Data Ingress Mesh & Live Telemetry Engine

An enterprise-grade, high-velocity clickstream telemetry pipeline designed to simulate big-tech operational infrastructures (FAANG standard). The framework orchestrates dynamic traffic routing, zero-trust perimeter firewalls, and real-time streaming math coupled with an Unsupervised Machine Learning layer for instantaneous threat pattern isolation.

---

## 🏗️ Architectural Topology Overview

The core system processes high-volume transactional streams through decoupled computational nodes to maintain sub-millisecond execution boundaries:

[Inbound Traffic Stream]
│
▼
┌──────────────────────┐
│  security_mesh.py    │ ──► Zero-Trust Signature Analysis & Ingress Firewall
└──────────────────────┘
│
▼
┌──────────────────────┐
│  load_balancer.py    │ ──► Round-Robin Multi-Shard Routing Layer
└──────────────────────┘
│
▼
┌──────────────────────┐
│     pipeline.py      │ ──► Online Unsupervised Machine Learning (Isolation Forest)
└──────────────────────┘
│
▼
┌──────────────────────┐
│    analytics.py      │ ──► Sliding Window Computational Math Engine
└──────────────────────┘
│
▼
┌──────────────────────┐
│   health_monitor.py  │ ──► Low-Level OS Thread & Resource Monitor
└──────────────────────┘
│
▼
┌──────────────────────┐
│    db_manager.py     │ ──► Fault-Tolerant Persistent State Store
└──────────────────────┘
│
▼
┌──────────────────────┐
│    dashboard.py      │ ──► High-Fidelity Cyberpunk NOC Command Center

└──────────────────────┘

---

## ⚡ Key System Capabilities

* **Distributed Sharding Logic:** Implements a robust `DistributedLoadBalancer` to evenly shard inbound requests across simulated cloud cluster nodes (`CLUSTER-US-EAST-01`, `CLUSTER-EU-WEST-02`, `CLUSTER-AP-SOUTH-03`).
* **Zero-Trust Security Perimeter:** Scans payloads using pre-compiled regex grids to intercept SQL Injection (SQLi), Cross-Site Scripting (XSS), and automated millisecond-level brute-force/DDoS volumes.
* **Unsupervised Isolation Matrix:** Utilizes an `Isolation Forest Ensemble` model to parse high-dimensional data arrays `[Interaction Clicks, System Time, Bounce Coefficient]` without manual classification rules.
* **Low-Level Hardware Profiling:** Hooks deep into OS process execution loops via `psutil` to extract real-time Sandbox Memory Resident Footprints (RSS), active execution threads, and hardware volatility matrices.

---

## 🧮 Statistical Mechanics & Core Math

To track structural distribution anomalies in the inbound packet logs without heavy computational locks, the system calculates real-time sliding-window statistics:

### 1. Dynamic Ingress Shannon Entropy $H(X)$
Monitors the distribution chaos of intercepted threat variations inside the routing node buffer:

$$H(X) = -\sum_{i=1}^{n} P(x_i) \log_2 P(x_i)$$

Where $P(x_i)$ represents the unique probability weight of a specific threat signature string. Sudden spikes in entropy flags automated matrix-bot deployment variants.

### 2. Rolling Standard Deviation Matrix ($\sigma$)
Tracks variance volatility inside the throughput pipeline across sliding chronological metrics:

$$\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2}$$

---

## 🛠️ Technical Stack & Framework Bindings

* **Language Platform:** Python 3 (Optimized for low-overhead multi-threading computations)
* **Core Machine Learning:** Scikit-Learn Ecosystem (`IsolationForest`)
* **Vector Analytics Core:** NumPy Processing Layer
* **Data Persistence Node:** Transactional SQLite Relational Engine
* **UI Control Plane:** Streamlit High-Fidelity Streaming Engine
* **System Worker Interface:** PSUtil Low-Level Kernel Bindings

---

## 🏎️ Deployment & Cluster Execution Manual

### Prerequisites
Ensure your infrastructure environment contains the mandatory dependencies:

pip install streamlit scikit-learn numpy psutil pandas

Initializing the Cloud Infrastructure Nodes
Fire up the Core Data Pipeline Engine (Backend Ingestion):


python pipeline.py
Expect Output Confirmation: ⚙️ [CORE COMPUTE NODE] Distributed Matrix boundaries mapped across Virtual Shards.

Launch the Network Operations Center Monitor (Frontend UI):


python -m streamlit run dashboard.py
Developed for distributed systems validation, AI/ML placement evaluation benchmarks, and massive scale data telemetry validation.


