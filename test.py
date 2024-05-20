# import streamlit as st
# import replicate
# import os
# from transformers import AutoTokenizer
# from gtts import gTTS
# import base64
# from streamlit_player import st_player

# # Set assistant icon to Snowflake logo
# icons = {"assistant": "./Snowflake_Logomark_blue.svg", "user": "⛷️"}

# # App title
# st.set_page_config(page_title="Snowflake Arctic")

# # Replicate Credentials
# with st.sidebar:
#     st.title('Snowflake Arctic')
#     if 'REPLICATE_API_TOKEN' in st.secrets:
#         replicate_api = st.secrets['REPLICATE_API_TOKEN']
#     else:
#         replicate_api = st.text_input('Enter Replicate API token:', type='password')
#         if not (replicate_api.startswith('r8_') and len(replicate_api) == 40):
#             st.warning('Please enter your Replicate API token.', icon='⚠️')
#             st.markdown("**Don't have an API token?** Head over to [Replicate](https://replicate.com) to sign up for one.")

#     os.environ['REPLICATE_API_TOKEN'] = replicate_api
#     st.subheader("Adjust model parameters")
#     temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.3, step=0.01)
#     top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)

# # Store LLM-generated responses
# if "messages" not in st.session_state.keys():
#     st.session_state.messages = [{"role": "assistant", "content": "Hi. I'm Arctic, a new, efficient, intelligent, and truly open language model created by Snowflake AI Research. Ask me anything."}]

# # Display or clear chat messages
# for message in st.session_state.messages:
#     with st.chat_message(message["role"], avatar=icons[message["role"]]):
#         st.write(message["content"])

# def clear_chat_history():
#     st.session_state.messages = [{"role": "assistant", "content": "Hi. I'm Arctic, a new, efficient, intelligent, and truly open language model created by Snowflake AI Research. Ask me anything."}]

# st.sidebar.button('Clear chat history', on_click=clear_chat_history)
# st.sidebar.caption('Built by [Snowflake](https://snowflake.com/) to demonstrate [Snowflake Arctic](https://www.snowflake.com/blog/arctic-open-and-efficient-foundation-language-models-snowflake). App hosted on [Streamlit Community Cloud](https://streamlit.io/cloud). Model hosted by [Replicate](https://replicate.com/snowflake/snowflake-arctic-instruct).')
# st.sidebar.caption('Build your own app powered by Arctic and [enter to win](https://arctic-streamlit-hackathon.devpost.com/) $10k in prizes.')

# @st.cache_resource(show_spinner=False)
# def get_tokenizer():
#     """Get a tokenizer to make sure we're not sending too much text
#     text to the Model. Eventually we will replace this with ArcticTokenizer
#     """
#     return AutoTokenizer.from_pretrained("huggyllama/llama-7b")

# def get_num_tokens(prompt):
#     """Get the number of tokens in a given prompt"""
#     tokenizer = get_tokenizer()
#     tokens = tokenizer.tokenize(prompt)
#     return len(tokens)

# # Function for generating Snowflake Arctic response
# def generate_arctic_response():
#     prompt = []
#     for dict_message in st.session_state.messages:
#         if dict_message["role"] == "user":
#             prompt.append("user\n" + dict_message["content"] + "")
#         else:
#             prompt.append("assistant\n" + dict_message["content"] + "")
    
#     prompt.append("assistant")
#     prompt.append("")
#     prompt_str = "\n".join(prompt)
    
#     if get_num_tokens(prompt_str) >= 3072:
#         st.error("Conversation length too long. Please keep it under 3072 tokens.")
#         st.button('Clear chat history', on_click=clear_chat_history, key="clear_chat_history")
#         st.stop()

#     for event in replicate.stream("snowflake/snowflake-arctic-instruct",
#                            input={"prompt": prompt_str,
#                                   "prompt_template": r"{prompt}",
#                                   "temperature": temperature,
#                                   "top_p": top_p,
#                                   }):
#         yield str(event)

# def text_to_speech(text):
#     tts = gTTS(text)
#     tts.save("response.mp3")
#     audio_file = open("response.mp3", "rb")
#     audio_bytes = audio_file.read()
#     audio_file.close()
#     audio_base64 = base64.b64encode(audio_bytes).decode()
#     return audio_base64

# # User-provided prompt
# if prompt := st.chat_input(disabled=not replicate_api):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user", avatar="⛷️"):
#         st.write(prompt)

# # Generate a new response if last message is not from assistant
# if st.session_state.messages[-1]["role"] != "assistant":
#     with st.chat_message("assistant", avatar="./Snowflake_Logomark_blue.svg"):
#         response = generate_arctic_response()
#         full_response = st.write_stream(response)
#         st.session_state.messages.append({"role": "assistant", "content": full_response})
        
#         # Convert the response to speech and play it
#         audio_base64 = text_to_speech(full_response)
#         st_player(f"data:audio/mp3;base64,{audio_base64}", playing=True)
import streamlit as st
import replicate
import os
from transformers import AutoTokenizer
from gtts import gTTS
import base64
from streamlit_player import st_player

# Set assistant icon to Snowflake logo
icons = {"assistant": "./Snowflake_Logomark_blue.svg", "user": "⛷️"}

# App title
st.set_page_config(page_title="Snowflake Arctic")

# Replicate Credentials
with st.sidebar:
    st.title('Snowflake Arctic')
    if 'REPLICATE_API_TOKEN' in st.secrets:
        replicate_api = st.secrets['REPLICATE_API_TOKEN']
    else:
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api) == 40):
            st.warning('Please enter your Replicate API token.', icon='⚠️')
            st.markdown("**Don't have an API token?** Head over to [Replicate](https://replicate.com) to sign up for one.")

    os.environ['REPLICATE_API_TOKEN'] = replicate_api
    st.subheader("Adjust model parameters")
    temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.3, step=0.01)
    top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)

# Store LLM-generated responses and user persona
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Hi. I'm Arctic, a new, efficient, intelligent, and truly open language model created by Snowflake AI Research. Ask me anything."}]
if "persona" not in st.session_state.keys():
    st.session_state.persona = {}

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=icons[message["role"]]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Hi. I'm Arctic, a new, efficient, intelligent, and truly open language model created by Snowflake AI Research. Ask me anything."}]

st.sidebar.button('Clear chat history', on_click=clear_chat_history)
st.sidebar.caption('Built by [Snowflake](https://snowflake.com/) to demonstrate [Snowflake Arctic](https://www.snowflake.com/blog/arctic-open-and-efficient-foundation-language-models-snowflake). App hosted on [Streamlit Community Cloud](https://streamlit.io/cloud). Model hosted by [Replicate](https://replicate.com/snowflake/snowflake-arctic-instruct).')
st.sidebar.caption('Build your own app powered by Arctic and [enter to win](https://arctic-streamlit-hackathon.devpost.com/) $10k in prizes.')

@st.cache_resource(show_spinner=False)
def get_tokenizer():
    """Get a tokenizer to make sure we're not sending too much text to the Model. Eventually we will replace this with ArcticTokenizer."""
    return AutoTokenizer.from_pretrained("huggyllama/llama-7b")

def get_num_tokens(prompt):
    """Get the number of tokens in a given prompt"""
    tokenizer = get_tokenizer()
    tokens = tokenizer.tokenize(prompt)
    return len(tokens)

def parse_persona_file(uploaded_file):
    """Parse the uploaded text file to extract persona information"""
    persona_data = {}
    for line in uploaded_file:
        key, value = line.decode('utf-8').strip().split(':', 1)
        persona_data[key.strip()] = value.strip()
    return persona_data

def apply_persona_to_prompt(prompt, persona):
    """Apply persona information to the prompt"""
    if persona:
        persona_intro = "\n".join([f"{key}: {value}" for key, value in persona.items()])
        prompt = f"{persona_intro}\n\n{prompt}"
    return prompt

# Function for generating Snowflake Arctic response
def generate_arctic_response():
    prompt = []
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            prompt.append("user\n" + dict_message["content"] + "")
        else:
            prompt.append("assistant\n" + dict_message["content"] + "")
    
    prompt.append("assistant")
    prompt.append("")
    prompt_str = "\n".join(prompt)
    
    prompt_str = apply_persona_to_prompt(prompt_str, st.session_state.persona)
    
    if get_num_tokens(prompt_str) >= 3072:
        st.error("Conversation length too long. Please keep it under 3072 tokens.")
        st.button('Clear chat history', on_click=clear_chat_history, key="clear_chat_history")
        st.stop()

    for event in replicate.stream("snowflake/snowflake-arctic-instruct",
                           input={"prompt": prompt_str,
                                  "prompt_template": r"{prompt}",
                                  "temperature": temperature,
                                  "top_p": top_p,
                                  }):
        yield str(event)

def text_to_speech(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    audio_file = open("response.mp3", "rb")
    audio_bytes = audio_file.read()
    audio_file.close()
    audio_base64 = base64.b64encode(audio_bytes).decode()
    return audio_base64

# Upload user persona file
uploaded_file = st.sidebar.file_uploader("Upload a text file with persona data", type=["txt"])
if uploaded_file:
    st.session_state.persona = parse_persona_file(uploaded_file)
    st.sidebar.success("Persona data loaded successfully!")

# User-provided prompt
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="⛷️"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant", avatar="./Snowflake_Logomark_blue.svg"):
        response = generate_arctic_response()
        full_response = st.write_stream(response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
        
        # Convert the response to speech and play it
        audio_base64 = text_to_speech(full_response)
        st_player(f"data:audio/mp3;base64,{audio_base64}", playing=True)
