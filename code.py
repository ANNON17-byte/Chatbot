from langgraph.graph import StateGraph,START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.checkpoint.memory import MemorySaver


load_dotenv()

model = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash'
)

from langgraph.graph.message import add_messages

class chat(TypedDict):

    message : Annotated[list[BaseMessage],add_messages]



def node(state: chat):

    message = state['message']

    response = model.invoke(message)

    return {'message' : [response]}



checkpointer = MemorySaver()

graph = StateGraph(chat)

graph.add_node('node',node)

graph.add_edge(START,'node')
graph.add_edge('node', END)

workflow = graph.compile(checkpointer=checkpointer)

