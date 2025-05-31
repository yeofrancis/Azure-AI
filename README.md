# 🌐 Azure AI | AI-102 Learning Labs & Proof of Concepts

This repository contains structured, hands-on Proof of Concepts (PoCs), prompt engineering examples, and resource setup guides aligned to the **Microsoft AI-102: Designing and Implementing a Microsoft Azure AI Solution**.

> 💡 Built with real-world use cases using **Azure OpenAI**, this repo bridges theory with practice and helps reinforce each learning objective through working code and design patterns.

---

## 🎯 Objective

To serve as a hands-on companion and learning guide for the [Microsoft Learn path](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/)  Each folder contains:
- A focused **use case or unit-based PoC**
- Relevant **code samples** (Python SDK or REST)
- Real-world **prompt engineering patterns**
- Azure resource setup or design considerations

---

## 🗂️ Repository Structure

| Folder | Description |
|--------|-------------|
| `codegen-poc/` | PoC that converts natural language to executable Python code using Azure OpenAI |
| `prompt-engineering-lab/` | Examples of few-shot prompting, role guidance, and context injection |
| `api-call-samples/` | SDK and REST API samples to invoke GPT and Codex models |
| `notebooks/` | Optional: Interactive Jupyter experiments (chat, summarization, classification) |
| `docs/` | Setup guides, exam notes, and reference material |

---

## 📘 Module-to-Folder Mapping (AI-102 Study Aid)

| Learn Module Unit | Repo Folder / File |
|-------------------|--------------------|
| Access Azure OpenAI | `docs/azure-openai-resource-setup.md` + `api-call-samples/` |
| Integrate OpenAI into an App | `api-call-samples/python-sdk.py` |
| Prompt Engineering | `prompt-engineering-lab/` |
| Provide Context with Prompts | `prompt-engineering-lab/few-shot-samples/` |
| Construct Code from Natural Language | `codegen-poc/app.py` |

---
## 🧪 How to Use This Repository

Each subfolder in this repository contains a self-contained PoC or lab aligned to an AI-102 topic or Microsoft Learn module.

To get started:

```bash
git clone https://github.com/yeofrancis/Azure-AI.git
cd Azure-AI/<module-folder>
```


## 🚀 Run the Code Generator

Run the following to To try the natural language:
```bash
## 🧪 Quick Start

```bash
git clone https://github.com/yeofrancis/Azure-AI.git
cd Azure-AI/codegen-poc
pip install -r requirements.txt
python app.py
