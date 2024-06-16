import streamlit as st
from src.pipeline.prediction_pipeline import prediction_pipeline
import time

st.title("Medical Chatbot")
st.caption("I assist you in diagnosing your symptoms")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Give at least 5 symptoms and the more symptoms you provide, the more accurately I can diagnose your issue."}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input()

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # Call the prediction pipeline
    pred = prediction_pipeline(str(prompt))
    msg = pred.disease_output()
    medication = pred.medication_output()
    
    #st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    
    # Store the predicted disease and medication in session state
    st.session_state["predicted_disease"] = msg
    st.session_state["medication"] = medication
    st.session_state["show_buttons"] = True
    st.session_state["Show"] = False

# Show Yes/No buttons if a disease has been predicted
if st.session_state.get("show_buttons"):
    #col1, col2 = st.columns(2)
    #with col1:
        if st.button("Yes"):
            st.session_state.messages.append({"role": "user", "content": "Yes"})
            st.chat_message("user").write("Yes")
            st.chat_message("assistant").write(st.session_state["medication"])
            st.session_state.messages.append({"role": "assistant", "content": st.session_state["medication"]})
            st.chat_message("assistant").write("Do have any modifications in symptoms or going to leave chat")
            st.session_state["Show"] = True

            #st.experimental_rerun()  # Rerun the app to show the medication response
    #with col2:
        elif st.button("No"):
            #st.chat_message("user").write("No")
            #st.chat_message("user").write("This chat will end in 10 seconds")
                        st.chat_message("user").write("No")
                        st.chat_message("assistant").write("Resting the session. Please No button")
                        #st.experimental_rerun()
                        for key in st.session_state.keys():
                            del st.session_state[key]
            
if st.session_state.get("Show"):
                #colm1, colm2 = st.columns(2)
                #with colm1:
                    if st.button("YES"):
                        st.session_state.messages.append({"role": "user", "content": "Yes"})
                        st.chat_message("user").write("Yes")
                        st.chat_message("assistant").write("Rest the current session and start new session to do so Please YES button once again")
                        for key in st.session_state.keys():
                            del st.session_state[key]
                #with colm2:
                    elif st.button("NO"):
                        st.chat_message("user").write("No")
                        st.chat_message("assistant").write("Resting the session. Please press previous NO button once again")
                        for key in st.session_state.keys():
                            del st.session_state[key]
