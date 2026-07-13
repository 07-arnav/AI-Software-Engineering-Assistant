

from fastapi import APIRouter
from app.prompts.system_prompts import SOFTWARE_ENGINEERING_SYSTEM_PROMPT
from app.ai.gemini import llm
from app.schemas.chat import ChatRequest, ChatResponse
from langchain_core.prompts import ChatPromptTemplate

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                SOFTWARE_ENGINEERING_SYSTEM_PROMPT,
            ),
            (
                "human",
                "{question}",
            ),
        ]
    )

    messages = prompt.format_messages(
        question=request.message
    )

    response = llm.invoke(messages)

    return ChatResponse(
        response=response.text()
    )