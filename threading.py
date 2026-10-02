import streamlit as st
from code import workflow
from langchain_core.messages import HumanMessage, AIMessage
import uuid


def generate_thread_id():
    return str(uuid.uuid4())


def add_thread(thread_id):
    if thread_id not in st.session_state["chat_threads"]:
        st.session_state["chat_threads"].append(thread_id)


def reset_chat():
    thread_id = generate_thread_id()
    st.session_state["thread_id"] = thread_id
    st.session_state["message_history"] = []
    add_thread(thread_id)


def load_conversation(thread_id):
    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    state = workflow.get_state(config=config)
    return state.values.get("message", [])


if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()

if "chat_threads" not in st.session_state:
    st.session_state["chat_threads"] = []

add_thread(st.session_state["thread_id"])


st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()
    st.rerun()

st.sidebar.header("My Conversations")

for thread_id in st.session_state["chat_threads"][::-1]:

    if st.sidebar.button(
        str(thread_id),
        key=f"thread_{thread_id}"
    ):

        st.session_state["thread_id"] = thread_id

        messages = load_conversation(thread_id)

        temp_messages = []

        for msg in messages:

            if isinstance(msg, HumanMessage):
                role = "user"

            elif isinstance(msg, AIMessage):
                role = "assistant"

            else:
                continue

            content = msg.content

            if isinstance(content, str):
                text = content

            elif isinstance(content, list):

                text = ""

                for item in content:

                    if (
                        isinstance(item, dict)
                        and item.get("type") == "text"
                    ):
                        text += item.get("text", "")

            else:
                text = str(content)

            temp_messages.append({
                "role": role,
                "content": text
            })

        st.session_state["message_history"] = temp_messages
        st.rerun()


for message in st.session_state["message_history"]:

    with st.chat_message(message["role"]):
        st.write(message["content"])


def stream_text(user_input):

    config = {
        "configurable": {
            "thread_id": st.session_state["thread_id"]
        }
    }

    for message_chunk, metadata in workflow.stream(
        {
            "message": [
                HumanMessage(content=user_input)
            ]
        },
        config=config,
        stream_mode="messages"
    ):

        if isinstance(message_chunk, AIMessage):

            content = message_chunk.content

            if isinstance(content, str):
                yield content

            elif isinstance(content, list):

                for item in content:

                    if (
                        isinstance(item, dict)
                        and item.get("type") == "text"
                    ):
                        yield item.get("text", "")


user_input = st.chat_input("Type here")

if user_input:

    st.session_state["message_history"].append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):

        ai_message = st.write_stream(
            stream_text(user_input)
        )

    st.session_state["message_history"].append({
        "role": "assistant",
        "content": ai_message
    })