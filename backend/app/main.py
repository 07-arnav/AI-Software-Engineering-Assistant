from fastapi import FastAPI

app = FastAPI(
    title="AI Software Engineering Assistant",
    description="An AI-powered assistant for developers.",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Software Engineering Assistant 🚀"
    }