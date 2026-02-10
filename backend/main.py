from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess

app = FastAPI(title="Offline AI Assistant")

# ✅ ADD THIS (CORS SUPPORT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (safe for local app)
    allow_credentials=True,
    allow_methods=["*"],  # allows OPTIONS, POST, etc.
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        result = subprocess.run(
            ["ollama", "run", "tinyllama"],
            input=req.message,
            text=True,
            capture_output=True,
            timeout=120
        )

        if result.returncode != 0:
            return {"error": result.stderr}

        return {
            "response": result.stdout.strip()
        }

    except Exception as e:
        return {"error": str(e)}
