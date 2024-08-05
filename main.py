from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Load API key and voice ID from environment variables
XI_API_KEY = os.getenv("XI_API_KEY")
VOICE_ID = os.getenv("VOICE_ID")

class TextToSpeechRequest(BaseModel):
    text: str
    stability: float = 0.5
    similarity_boost: float = 0.8
    style: float = 0.0
    use_speaker_boost: bool = True

@app.post("/convert-to-speech/")
async def convert_to_speech(request: TextToSpeechRequest):
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    headers = {
        "Accept": "application/json",
        "xi-api-key": XI_API_KEY
    }
    data = {
        "text": request.text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": request.stability,
            "similarity_boost": request.similarity_boost,
            "style": request.style,
            "use_speaker_boost": request.use_speaker_boost
        }
    }
    response = requests.post(tts_url, headers=headers, json=data, stream=True)
    if response.ok:
        with open("output.mp3", "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        return {"message": "Audio stream saved successfully.", "audio_path": "output.mp3"}
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)





# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# app = FastAPI()

# # Load API key from environment variables
# XI_API_KEY = os.getenv("XI_API_KEY")
# print(XI_API_KEY)

# class TextToSpeechRequest(BaseModel):
#     text: str
#     voice_id: str
#     stability: float = 0.5
#     similarity_boost: float = 0.8
#     style: float = 0.0
#     use_speaker_boost: bool = True

# @app.post("/convert-to-speech/")
# async def convert_to_speech(request: TextToSpeechRequest):
#     tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{request.voice_id}/stream"
#     headers = {
#         "Accept": "application/json",
#         "xi-api-key": XI_API_KEY
#     }
#     data = {
#         "text": request.text,
#         "model_id": "eleven_multilingual_v2",
#         "voice_settings": {
#             "stability": request.stability,
#             "similarity_boost": request.similarity_boost,
#             "style": request.style,
#             "use_speaker_boost": request.use_speaker_boost
#         }
#     }
#     response = requests.post(tts_url, headers=headers, json=data, stream=True)
#     if response.ok:
#         with open("output.mp3", "wb") as f:
#             for chunk in response.iter_content(chunk_size=1024):
#                 f.write(chunk)
#         return {"message": "Audio stream saved successfully.", "audio_path": "output.mp3"}
#     else:
#         raise HTTPException(status_code=response.status_code, detail=response.text)

