from backend.ai.router import ai_request
from backend.history.history_retriever import search_history
from backend.history.history_manager import new_conversation_file, save_message
from backend.history.history_classifier import classification

def main():
    file_path=None
    while True:
        user_input=str(input("You: "))
        if(user_input=="exit"):
            break

        if(file_path==None):
            file_path=new_conversation_file(user_input)

        if(user_input!="exit"):
            classification_result=classification(user_input)
            save_message(file_path, {"role": "user", "content": user_input})

            if(classification_result=="history needed" or classification_result==None):
                retrieved_relevent_history=search_history(user_input)
                try:
                    response=ai_request(user_input, retrieved_relevent_history)
                    print(response)
                    save_message(file_path, {"role": "assistant", "content": response})
                except RuntimeError:
                    print("All AI providers failed.")

            elif(classification_result=="history not needed"):
                try:
                    response=ai_request(user_input, None)
                    print(response)
                    save_message(file_path, {"role": "assistant", "content": response})
                except RuntimeError:
                    print("All AI providers failed.")

if(__name__=="__main__"):
    main()