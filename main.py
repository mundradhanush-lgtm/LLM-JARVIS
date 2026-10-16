from backend.ai.router import ai_request

def main():
    user_input = input("You: ")
    try:
        response = ai_request(user_input)
        print(response)
    except RuntimeError:
        print("All AI providers failed.")

if(__name__=="__main__"):
    main()