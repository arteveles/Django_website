import streamlit as st
from gigachat_api import send_prompt, get_access_token


st.title("Чат бот")

if "access_token" not in st.session_state:
    try:
        st.session_state.access_token = get_access_token()
        st.toast(f"Получен токен")
    except Exception as e:
        st.toast(f"Не получен токен")

if "messages" not in st.session_state:
    # переменная для хранения сессии чата
    st.session_state.messages = [{
        "role": "ai",
        "content": "С чем Вам помочь?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# что отправлять в чат бот?
if user_prompt := st.chat_input():
    st.chat_message("user").write(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.spinner("В процессе ..."):
        response = send_prompt(user_prompt, st.session_state.access_token)
        st.toast(response)

        st.chat_message("ai").write(response)
        st.session_state.messages.append({"role": "ai", "content": response})