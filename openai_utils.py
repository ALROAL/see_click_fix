import openai
import re
import os

openai.api_key = os.environ["OPENAI_API_KEY"]
def get_priority_and_explanation(title, description):
    
    

    message = f"You are responsible for prioritizing the reports from residents relative to non-emergency issues around the city. \
        You will be asked to rank the severity/urgency of the reported issues from 1 (low) to 10 (high). \
        Rank the severity of the following incident report from 1 (low) to 10 (high). \
        \n Title: {title} \n Description: {description} \
        \n The severity score must be given in the format 'Severity Score: <score>' Additionally, provide a short and direct explanation for your answer \
        in a single paragraph. Do not refer to the severity score when giving the explanation. The explanation must be given in the format 'Explanation: <explanation>'"
    
    response = openai.ChatCompletion.create(
                                model="gpt-3.5-turbo",
                                messages = [{"role": "user", "content": message}],
                                max_tokens=100
                                )

    response_text = response["choices"][0]["message"]["content"]
    priority_score = int(re.search("(?<=Severity Score: )[0-9]*", response_text).group(0))
    explanation = re.search("(?<=Explanation: ).*", response_text).group(0)

    return priority_score, explanation