from google import genai
from google.genai.errors import ClientError, ServerError
import httpx
from api_keys import gemini_client

try:
    user_input=str(input("INPUT PLEASE: "))
    response=gemini_client.models.generate_content(
        model="gemini-3.8-flash",
        contents=user_input
    )
    print(response.text)
except ClientError as e:
    status_code=e.code

    if(status_code==400):
        print("Bad Request:	The request is invalid, has malformed data, or contains an unsupported parameter.")
    elif(status_code==401):
        print("Unauthorized: The API key is missing, invalid, or not accepted.")
    elif(status_code==403):
        print("Forbidden: The key or account doesn't have permission to access the requested resource.")
    elif(status_code==404):
        print("Not Found: The model name or requested resource doesn't exist or isn't available at that endpoint.")
    elif(status_code==405):
        print("Method Not Allowed: The HTTP method used isn't supported for that endpoint.")
    elif(status_code==408):
        print("Request Timeout: The server timed out while waiting for the request.")
    elif(status_code==409):
        print("Conflict: The request conflicts with the current state of a resource.")
    elif(status_code==410):
        print("Gone: The requested resource is no longer available.")
    elif(status_code==413):
        print("Content Too Large: The request payload is too large.")
    elif(status_code==415):
        print("Unsupported Media Type: The request uses a content format the endpoint doesn't support.")
    elif(status_code==422):
        print("Unprocessable Entity: The request format may be valid, but its contents can't be processed.")
    elif(status_code==429):
        print("Too Many Requests: You've exceeded a rate limit or quota, or are sending requests too quickly.")
    else:
        print("An unexpected error has occured")

except ServerError as e:
    status_code = e.code

    if(status_code==500):
        print("Internal Server Error: The server encountered an unexpected problem while processing your request.")
    elif(status_code==501):
        print("Not Implemented: The server doesn't support the functionality required to process the request.")
    elif(status_code==502):
        print("Bad Gateway: A gateway or proxy received an invalid response from another server.")
    elif(status_code==503):
        print("Service Unavailable: The service is temporarily unavailable, possibly due to maintenance or overload.")
    elif(status_code==504):
        print("Gateway Timeout:	A gateway or proxy waited too long for another server to respond.")
    else:
        print("An unexpected error has occured")

except httpx.RequestError as e:
    print(f"Network error: Unable to connect to AI service")