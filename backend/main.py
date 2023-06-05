#uvicorn main:app --reload


from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai


# Custom Functions IMports
from functions.database import store_messages, reset_messages
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.text_to_speech import conver_text_to_speech


# Initiate APP
app = FastAPI()


# CORS - Origins
origins = [
<<<<<<< HEAD
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "http://192.168.1.106",
    "http://192.168.1.106:3000",
    "*",
=======
    "http://127.0.0.1:3000"
>>>>>>> parent of 4a3faa8 (done)
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



<<<<<<< HEAD
# post bot response
@app.post("/post-audio")
async def post_audio(file: UploadFile=File(...)):

    # Get saved audio 
    audio_input = open("voice.mp3", "rb")

    # # Save file from frontend
    # with open(file.filename, "wb") as buffer:
    #     buffer.write(file.file.read())
    # audio_input = open(file.filename, "rb")
=======
# get bot response
@app.get("/get-audio/")
async def get_audio():

    # Get saved audio 
    audio_input = open("voice.mp3", "rb")
>>>>>>> parent of 4a3faa8 (done)

    # Decode Audio 
    message_decoded = convert_audio_to_text(audio_input)

    # Guard: Ensure message decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail="failed to decode audio")
    
    
    # Get ChatGPT Response
    chat_response = get_chat_response(message_decoded)

    # Guard: Ensure chat_response
    if not chat_response:
        return HTTPException(status_code=400, detail="failed to get chat response")
    
    # Store messages
    store_messages(message_decoded, chat_response)


    # Convert chat resposne to audio
    audio_output = conver_text_to_speech(chat_response)

    # Guard: Ensure audio_output
    if not audio_output:
        return HTTPException(status_code=400, detail="failed to get Eleven Labs response")
    

    def iterfile():
        yield audio_output
    
    return StreamingResponse(iterfile(), media_type="audio/mpeg")