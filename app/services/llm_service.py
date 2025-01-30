import openai
import logging
from app.core.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_tone_sentiment(text: str, stars: int):
    """
    Generate tone and sentiment analysis for a given review using OpenAI's GPT-3.5-Turbo.
    
    Args:
        text (str): The review text.
        stars (int): The star rating of the review.
    
    Returns:
        tuple: (tone, sentiment) strings or (None, None) in case of an error.
    """
    try:
        prompt = (
            f"Analyze this review: '{text}' with {stars} stars. "
            "Provide the tone and sentiment as a semicolon-separated string (tone; sentiment)."
        )
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        
        result = response["choices"][0]["message"]["content"].strip()
        
        if ";" in result:
            tone, sentiment = result.split(";", 1)
            return tone.strip(), sentiment.strip()
        else:
            logging.error("Unexpected response format: %s", result)
            return None, None
    
    except Exception as e:
        logging.error("Error in LLM sentiment analysis: %s", str(e))
        return None, None
