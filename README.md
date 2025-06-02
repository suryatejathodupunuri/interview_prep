

---

# 💼 Interview Prep Assistant

Welcome to **Interview Prep**, an intelligent multi-agent system designed to help users practice and improve their interview skills. This project uses the MOYA framework combined with Ollama and large language models (LLMs) like `mistral` to simulate realistic interview scenarios and provide insightful feedback using AI agents.

---

## 🚀 Features

* Multi-agent architecture using MOYA
* AI-powered question generation and feedback via Ollama
* Technical, behavioral, and feedback agents
* Shared memory
* Central orchestrator to manage agent workflows

---

## 🛠️ Getting Started

### 1. Clone Git Repository

```bash
git clone https://github.com/suryatejathodupunuri/interview_prep.git
cd interview_prep
```

### 2. Install Dependencies

Install MOYA with Ollama support:

```bash
pip install moya-ai[ollama]
```

### 3. Set Up Ollama

Make sure you have [Ollama](https://ollama.com/download) installed and running.

Pull the required model (e.g., mistral):

```bash
ollama pull mistral
```

You should see something like:

```
mistral:latest    f974a74358d6    4.1 GB
```

---

## ⚙️ How to Run

Ensure Ollama is running and the model is loaded. Then run:

```bash
python main.py
```

The orchestrator will:

* Initiate all agents
* Share memory between them
* Ask technical and behavioral questions
* Collect responses
* Provide feedback with improvement suggestions

---

## 📦 Requirements

### `requirements.txt`

```text
moya-ai[ollama]
```
