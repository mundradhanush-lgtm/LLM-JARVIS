from google.genai.errors import ServerError
import httpx
import time
from api_keys import gemini_client

def gemini_request(user_input):

    attempts=3

    for attempt in range(1, attempts+1):
        try:
            response=gemini_client.models.generate_content(
                model="gemini-3.8-flash",
                contents=user_input
            )
            return response.text

        except ServerError as e:
            if(e.code not in(500, 502, 503, 504)):
                raise
            if(attempt==attempts):
                raise
            time.sleep(2)
        except httpx.RequestError:
            if(attempt==attempts):
                raise
            time.sleep(2)

if(__name__=="__main__"):
    user_input=str(input("INPUT PLEASE: "))
    print(gemini_request(user_input))