import streamlit as st
from code import workflow
from langchain_core.messages import HumanMessage


thread_id = "1"

config = {
    "configurable": {
        "thread_id": thread_id
    }
}

if "messagehis" not in st.session_state:
    st.session_state["messagehis"] = []


for message in st.session_state["messagehis"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def stream_text(user_input):

    for message_chunk, metadata in workflow.stream(
        {
            "message": [
                HumanMessage(content=user_input)
            ]
        },
        config=config,
        stream_mode="messages"
    ):

        content = message_chunk.content

        # Normal string content
        if isinstance(content, str):
            yield content

        # Gemini content blocks
        elif isinstance(content, list):

            for item in content:

                if isinstance(item, dict) and item.get("type") == "text":
                    yield item.get("text", "")


user_input = st.chat_input("Type here")


if user_input:
    st.session_state["messagehis"].append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):

        ai_mess = st.write_stream(
            stream_text(user_input)
        )

    st.session_state["messagehis"].append({
        "role": "assistant",
        "content": ai_mess
    })