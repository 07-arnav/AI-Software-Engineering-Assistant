from fastapi import APIRouter
from app.ai.gemini import llm

router = APIRouter()

@router.get("/chat")
def chat():
    try:
        response = llm.invoke("Say only: Hello Arnav")
        return {
            "response": response.text()
        }

    except Exception as e:
        return {
            "error": str(e),
            "error_type": type(e).__name__
        }