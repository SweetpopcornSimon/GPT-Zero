import nltk
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE
from utils import *

import openai

openai.api_key = "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"
model_engine = "text-davinci-002"


# Get the text input from the js server
def get_answer(prompt): 
    prompt = prompt + " give as many informations as you can about this, write about 10000 words"

    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=2000, n=1,stop=None,temperature=0.5)

    response = completions.choices[0].text
    return response