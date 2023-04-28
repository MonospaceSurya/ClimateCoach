import streamlit as st
import openai
import streamlit as st

from streamlit_chat import message
from llm import llmm




openai.api_key="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"
st.title("chatBot : Streamlit + openAI")

def generate_response(prompt):
    return llmm(prompt)

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
