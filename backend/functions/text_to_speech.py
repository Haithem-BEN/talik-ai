import requests

from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")

# Eleven Labs
# Convert text to speech
def conver_text_to_speech(message):

    voice_id = "xBCXR3YDVAxxCtuQHOAe"

    # API Request
    body = {
        "text": message,
        "voice_settings": {
            "stability": 1,
            "similarity_boost": 1,
        }
    }
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVEN_LABS_API_KEY
    }
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    # Send request
    try:
        response = requests.post(endpoint, json=body, headers=headers)
    except Exception as e:
        print(e)

    # Handle response
    if response.status_code == 200:
        return response.content
    else:
        return

    
