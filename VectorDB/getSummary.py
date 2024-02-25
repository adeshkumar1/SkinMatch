import os
from openai import OpenAI

def getSummary(level, skin):

    client = OpenAI(
        api_key = "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"
    )
    complete = client.chat.completions.create(
        messages = [
            {
                "role": "user", 
                "content": "This person has level " + str(level + 1) + " acne and " + skin + " skin. Similar to a doctor, create a " + 
                "response describing what this person has. Sample statement: Based on your images, you have _ acne and _ skin " +
                "Something personal like advice or rec. No longer than 50 words",
             }
            ],   
        model = "gpt-3.5-turbo", 
    )
    print(complete.choices[0].message)    
    #return complete.choices[0].message
    
getSummary(5,"dry")