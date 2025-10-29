from xai_sdk import Client
from xai_sdk.chat import system, user
from core.config import settings

class ChatService:
  def __init__(self):
    self.client = Client(
      api_key = settings.XAI_API_KEY,
      management_api_key = settings.MANAGEMENT_API_KEY,
      timeout = 3600
    )

  def search_policies(self, query: str):
    return self.client.collections.search(
      query=query,
      collection_ids=[settings.COLLECTION_ID]
    )
  
  def create_chat(self, context: str):
    return self.client.chat.create(
      model=settings.AI_MODEL,
      messages=[
        system("You are a chatbot that simplifies HR responses in a formal tone, under 60 words."),
        user(context)
      ]
    )