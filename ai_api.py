from openai import OpenAI

OpenAI.api_key = "api-key"
def ai(command):
    client = OpenAI()


    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "you are a person named naveen who speak english and hindi and you are his created chatbot i provide you old message and then you replies according to them.",
                "content": "Write a haiku about recursion in programming."
            }
        ]
    )
    return (completion.choices[0].message)