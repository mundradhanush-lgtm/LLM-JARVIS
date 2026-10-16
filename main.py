from backend.ai.router import ai_request

def main():
    while True:
        user_input=str(input("You: "))
        if(user_input=="exit"):
            break
        else:
            try:
                response = ai_request(user_input)
                print(response)
            except RuntimeError:
                print("All AI providers failed.")

if(__name__=="__main__"):
    main()