#uvicorn main:app --reload


from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai


# Custom Functions IMports
from functions.openai_requests import convert_audio_to_text


# Initiate APP
app = FastAPI()


# CORS - Origins
origins = [
    "http://127.0.0.1:3000"
]


# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Check Health 
@app.get("/health")
async def check_health():
    return {"message": "healthy"}


# Post bot response
@app.get("/post-audio/")
async def post_audio():
    audio_input = open("voice.mp3", "rb")

    # Decode Audio 
    message_decoded = convert_audio_to_text(audio_input)
    
    print(message_decoded)

    return "Done"