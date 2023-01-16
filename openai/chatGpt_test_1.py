import openai

import os


#openai.api_key = os.getenv["OPENAI_API_KEY"]
openai.api_key = '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'
prompt = "formatted strings in python"
completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text
print(message)