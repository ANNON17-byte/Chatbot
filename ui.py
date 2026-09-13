import streamlit as st
from code import workflow
from langchain_core.messages import HumanMessage

thread_id = '1'

config = {
        'configurable' : {'thread_id' : thread_id}
    }

if 'messagehis' not in st.session_state:
    st.session_state['messagehis'] = []
    


for message in st.session_state['messagehis']:
    with st.chat_message(message['role']):
        st.text(message['content'])
     
input = st.chat_input('Type here')


if(input):
    st.session_state['messagehis'].append({'role':'human','content' : input })
    with st.chat_message('human'):
        st.text(input)

    response = workflow.invoke({'message' : [HumanMessage(content=input)]},config=config)  
    ai =  response['message'][-1].content[0]['text']  
    st.session_state['messagehis'].append({'role':'ai','content' : ai })    
    with st.chat_message('ai'):
        st.text(ai)