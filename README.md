# Offline AI Assistant 🤖

An **offline AI assistant** built using **FastAPI**, **Ollama (local LLM)**, and **Flutter Web**.  
This project allows users to chat with an AI model **completely offline**, without relying on any cloud APIs.

---

## 🚀 Features

- ✅ Fully **offline AI chat**
- ✅ Uses **Ollama** for local LLM inference
- ✅ **FastAPI** backend for API handling
- ✅ **Flutter Web** frontend (works without OpenGL)
- ✅ Simple REST API (`/chat`)
- ✅ Clean and modular architecture
- ✅ Cross-platform (runs on Linux, browser-based UI)

---

## 🏗️ Architecture

Browser (Flutter Web UI)
|
| HTTP POST
v
FastAPI Backend (localhost:8000)
|
v
Ollama (Local LLM - TinyLlama)

## 📁 Project Structure
offline_ai_assistant/
├── backend/ # FastAPI backend
│ ├── main.py
│ └── venv/
├── frontend/ # Flutter Web UI
│ └── private_ai_ui/
├── model/ # (ignored) local LLM models
├── .gitignore
└── README.md

> ⚠️ Large model files and virtual environments are excluded from GitHub using `.gitignore`.

---

## ⚙️ Requirements

### Backend
- Python 3.10+
- Ollama installed
- FastAPI
- Uvicorn

### Frontend
- Flutter SDK (stable)
- Chrome browser (for Flutter Web)

---

## 🔧 Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
