from backend.ai.router import ai_request
from backend.history.history_manager import new_conversation_file, save_message

def main():
    file_path=None
    while True:
        user_input=str(input("You: "))
        if(user_input=="exit"):
            break
        if(file_path==None):
            file_path=new_conversation_file(user_input)
        save_message(file_path, {"role": "user", "content": user_input})
        try:
            response = ai_request(user_input)
            print(response)
            save_message(file_path, {"role": "assistant", "content": response})
        except RuntimeError:
            print("All AI providers failed.")

if(__name__=="__main__"):
    main()