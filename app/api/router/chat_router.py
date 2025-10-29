from fastapi import APIRouter, HTTPException
from schemas.chat_schema import ChatRequest, ChatResponse
from services.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["Chat"])
chat_service = ChatService()

@router.post("/", response_model=ChatResponse)
def chat_with_ai(payload: ChatRequest):
  try:
    search = chat_service.search_policies(payload.query)
    context = "\n".join([m.chunk_content for m in search.matches])
    chat = chat_service.create_chat(context)

    response_text = ""
    for response, chunk in chat.stream():
      response_text += chunk.content
    return ChatResponse(reply = response_text.strip())
  
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))