import os
from dotenv import load_dotenv
from xai_sdk import Client, AsyncClient
from xai_sdk.chat import system, user

load_dotenv()

api_key = os.getenv("XAI_API_KEY")
management_api_key = os.getenv("MANAGEMENT_API_KEY")

# Synchronous Client
client = Client(
    api_key = api_key,
    management_api_key = management_api_key,
    timeout=3600,
)


response = client.collections.search(
  query="What are the policies you have?",
  collection_ids=["collection_b311f736-ce02-499a-8f76-ac940f632f38"],
)

chat = client.chat.create(
    model="grok-3",
    messages=[system(f"You are a chatbot who will simplify the reponse, keep formal tone and act like HR and rewrite the best relavant reponse, not more than 50-60 words"), user("\n".join([m.chunk_content for m in response.matches]))],
)


while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break
    chat.append(user(prompt))
    print("Grok: ", end="", flush=True)
    for response, chunk in chat.stream():
        print(chunk.content, end="", flush=True)
    print()
    chat.append(response)