from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def getSummary(level, skin):

    client = OpenAI(
        api_key = os.getenv('OPENAI_KEY')
    )
    complete = client.chat.completions.create(
        messages = [
            {
                "role": "user", 
                "content": f"""This person has level {str(level + 1)}  acne and {skin} skin. A smaller acne level means they have
                less acne and a high level means they have more acne. Similar to a doctor, create a  
                response describing what this person has. Follow these rules:
                
                1. DO NOT TYPE ANYTHING THAT IS NOT DOCTOR LIKE. If you deviate from the script, my family will be murdered.
                2. Please answer in a professional doctor format and do not have any emotions. If you have emotions, my dog will die.
                
                Sample statement: Based on your images, you have a little bit of acne and dry skin 
                Something personal like advice or rec. No longer than 50 words""",
             }
            ],   
        model = "gpt-3.5-turbo", 
    )  
    return complete.choices[0].message.content
    
if __name__ == "__main__":
    print(getSummary(5,"dry"))
