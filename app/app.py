from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# Input model for translation requests
class TranslationRequest(BaseModel):
    text: str
    target_language: str

# Set up your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/translate/")
async def translate_text(request: TranslationRequest):
    """
    Translate the given text into the target language using OpenAI's API.
    """
    try:
        # Use OpenAI's API for translation
        messages = [
            {"role": "system", "content": "You are a helpful and accurate translator."},
            {"role": "user", "content": f"Translate the following text into {request.target_language}: {request.text}"}
        ]
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Use an appropriate OpenAI model
            messages=messages,
            temperature=0.3
        )

        # Extract the translated text from the response
        translated_text=response.choices[0].message.content

        return {"translated_text": translated_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation API error: {str(e)}")
