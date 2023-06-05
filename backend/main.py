#uvicorn main:app --reload


from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai


# Custom Functions IMports
from functions.database import store_messages, reset_messages
from functions.openai_requests import convert_audio_to_text, get_chat_response


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

    
# Check Health 
@app.get("/reset_messages")
async def check_health():
    reset_messages()
    return {"message": "conversations reseted"}


    


# get bot response
@app.get("/get-audio/")
async def get_audio():

    # Get saved audio 
    audio_input = open("voice.mp3", "rb")

    # Decode Audio 
    message_decoded = convert_audio_to_text(audio_input)

    # Guard: Ensure message decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail="failed to decode audio")
    
    # Get ChatGPT Response
    chat_response = get_chat_response(message_decoded)
    
    # Store messages
    store_messages(message_decoded, chat_response)
    
    print(chat_response)

    return "Done"