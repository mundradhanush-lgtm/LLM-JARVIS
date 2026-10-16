from groq import APIConnectionError, APIStatusError, RateLimitError
import time
from api_keys import groq

def groq_request(user_input):

    attempts=3
    for attempt in range(1, attempts+1):
        try: 
            response=groq.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                    "role":"user",
                    "content":user_input
                    }
                ]
            )
            return response.choices[0].message.content
        except APIConnectionError:
            if(attempt==attempts):
                raise
            time.sleep(2)
        except RateLimitError:
            raise
        except APIStatusError as e:
            if(e.code not in (500, 502, 503, 504)):
                raise
            if(attempt==attempts):
                raise
            time.sleep(2)

if(__name__=="__main__"):
    user_input=str(input("INPUT PLEASE: "))
    print(groq_request(user_input))