import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough

from elevenlabs.client import ElevenLabs
from elevenlabs import play


# Load environment variables from .env file

load_dotenv()


model = ChatOpenAI (model="gpt-3.5-turbo")

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Always respond in {language}",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

from langchain_core.runnables import RunnablePassthrough


def filter_messages(messages, k=10):
    return messages[-k:]


chain = (
    RunnablePassthrough.assign(messages=lambda x: filter_messages(x["messages"]))
    | prompt
    | model
)

with_message_history = RunnableWithMessageHistory(
    chain, 
    get_session_history,
    input_messages_key="messages"
    )

def get_chatbot_response(transcription):

    config = {"configurable": {"session_id": "abc2"}}

    response = with_message_history.invoke(
        {"messages":[HumanMessage(content=transcription)], "language":"Informal Bahasa Indonesia"},
        config=config,
    )

    return response.content

if __name__ == "__main__":
    # Standalone test block
    transcription = "Can you tell me some fun things to do in Jakarta"  # Example input for testing
    response = get_chatbot_response(transcription)
    print("Chatbot Response:", response)