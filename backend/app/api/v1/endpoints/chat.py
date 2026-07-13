from fastapi import APIRouter

from app.ai.gemini import llm
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    response = llm.invoke(request.message)

    return ChatResponse(
        response=response.text
    )