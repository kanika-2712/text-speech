import streamlit as st
import requests

st.title("Text-to-Speech")

text = st.text_area("Enter text to convert to speech:")
st.slider("Stability", 0.0, 1.0, 0.5, 0.1, key="stability_slider")
st.slider("Similarity Boost", 0.0, 1.0, 0.8, 0.1, key="similarity_boost_slider")
st.slider("Style", 0.0, 1.0, 0.0, 0.1, key="style_slider")
use_speaker_boost = st.checkbox("Use Speaker Boost", value=True, key="use_speaker_boost")

if st.button("Convert"):
    if text:
        response = requests.post(
            "http://127.0.0.1:8000/convert-to-speech/",
            json={
                "text": text,
                "stability": st.session_state.stability_slider,
                "similarity_boost": st.session_state.similarity_boost_slider,
                "style": st.session_state.style_slider,
                "use_speaker_boost": use_speaker_boost
            }
        )
        result = response.json()
        if "audio_path" in result:
            st.success(result["message"])
            st.audio(result["audio_path"], format="audio/mp3")
        else:
            st.error("Error converting text to speech.")
    else:
        st.warning("Please enter text.")



# import streamlit as st
# import requests
# import os

# st.title("Text-to-Speech")

# text = st.text_area("Enter text to convert to speech:")

# # Dropdown for voice selection
# voices = ["Voice 1", "Voice 2", "Voice 3"]  
# selected_voice = st.selectbox("Select Voice", voices)

# # Convert dropdown selection to voice ID or name for backend
# voice_id_mapping = {
#     "Voice 1": "EXAVITQu4vr4xnSDxMaL",
#     "Voice 2": "JBFqnCBsd6RMkjVDRZzb",
#     "Voice 3": "TX3LPaxmHKxFdv7VOQHJ"
# }
# selected_voice_id = voice_id_mapping.get(selected_voice, "default_voice_id")

# if st.button("Convert"):
#     if text:
#         response = requests.post(
#             "http://127.0.0.1:8000/convert-to-speech/",
#             json={
#                 "text": text,
#                 "voice_id": selected_voice_id
#             }
#         )
#         result = response.json()
#         if "audio_path" in result:
#             st.success(result["message"])
#             st.audio(result["audio_path"], format="audio/mp3")
#         else:
#             st.error("Error converting text to speech.")
#     else:
#         st.warning("Please enter text.")
