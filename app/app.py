from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import openai
import os

# Load environment variables from.env file
load_dotenv()

app = FastAPI()


# Input model for translation requests
class TranslationRequest(BaseModel):
    object: object
    target_language: str


# Set up your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.post("/translate")
async def translate_object(request: TranslationRequest):
    """
    Translate the given object into the target language using OpenAI's API.
    """
    try:
        # Use OpenAI's API for translation
        messages = [
            {"role": "system", "content": "You are a helpful and accurate translator."},
            {
                "role": "user",
                "content": f"Translate the following object into {request.target_language}. Do not change the structure of the object and do not add any additional text or information: {request.object}",
            },
        ]
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Use an appropriate OpenAI model
            messages=messages,
            temperature=0.3,
        )

        # Extract the translated text from the response
        translated_text = response.choices[0].message.content
        translated_object = eval(translated_text)  # Reconstruct the original object

        return {"translated_object": translated_object}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation API error: {str(e)}")
