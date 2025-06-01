# 🚀 Azure OpenAI Model Deployment Guide

This guide explains how to deploy OpenAI models such as `gpt-4o` into your Azure OpenAI resource using the Azure CLI. This step is required **before** calling the model from any application (e.g., Python PoCs like the code generator).

---

## 📦 Prerequisites

- An **Azure subscription**
- The **Azure OpenAI resource** created in a supported region (e.g., East US, West Europe)
- Access to Azure CLI (Cloud Shell or local)

---

## 🔧 Step-by-Step Deployment (gpt-4o)

### ✅ Deploy using Azure CLI:

Run this command in **Azure Cloud Shell** or your local terminal:

```bash
az cognitiveservices account deployment create \
  -g rg-azureai-poc \
  -n azai-gencode \
  --deployment-name gpt4o-codegen \
  --model-name gpt-4o \
  --model-version 2024-05-13 \
  --model-format OpenAI \
  --sku-name Standard \
  --sku-capacity 5

🧪 Verify the deployment:

```bash
az cognitiveservices account deployment show \
  -g rg-azureai-poc \
  -n azai-gencode \
  --deployment-name gpt4o-codegen \
  --output json

🛠️ Environment Setup

Add the following variables in a .env file or export them in your terminal:

```
AZURE_OPENAI_KEY=<your-api-key>
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt4o-codegen
