#llm api call logic-this calls groq api to get the response from the llm
#text->llm->response

import os
from groq import Groq #llm
from dotenv import load_dotenv #for loading env variables


load_dotenv() #reads the .env files

client=Groq(api_key=os.getenv("GROQ_API_KEY")) #initializing the client with the api key from env variables

def calling_llm(prompt):
    #sending request to the llm(.create) and getting the response
    response=client.chat.completions.create(
        #choosing llama because its open source and free to use-take in long text,smaller and faster 
        #reccommended on groq's documentation
        model="llama-3.1-8b-instant",
        messages=[
            {"role":"user","content":prompt}
        ],
        #controls the randomness of the response
        #low temperature->more focused response as model sticks to the rules
        temperature=0.2, 
    ) 
    #return the first out of the list of token choices
    return response.choices[0].message.content