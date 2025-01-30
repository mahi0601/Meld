import openai

def generate_tone_sentiment(text, stars):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Analyze the following review."},
            {"role": "user", "content": f"Review: {text}, Stars: {stars}"}
        ],
    )
    result = response["choices"][0]["message"]["content"]
    return result.split("|") 