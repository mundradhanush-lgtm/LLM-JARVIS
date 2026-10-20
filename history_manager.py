import json
from pathlib import Path

def new_conversation_file(user_input):
    input_list=user_input.split()
    input_list=input_list[0:6]
    underscored_user_input="_".join(input_list)
    lower_and_underscored_user_input=underscored_user_input.lower()

    sessions_dir=Path(__file__).parent/"sessions"
    sessions_dir.mkdir(exist_ok=True)
    session_files=sessions_dir.iterdir()
    session_number=0
    for i in session_files:
        if(i.is_file()==False):
            continue
        if(i.is_file()):
            file_name=i.name
            if(file_name.startswith("session")):
                parts=file_name.split("_", 1)
                file_number=parts[0].removeprefix("session")
                file_number=int(file_number)
                if(file_number>session_number):
                    session_number=file_number
            
    session_number+=1
    file_path=sessions_dir/f"session{session_number}_{lower_and_underscored_user_input}.json"
    with open(file_path, "x") as f:
        json.dump({"messages":[]}, f, indent=4)
    return file_path

def save_message(file_path, message):
    with open(file_path, "r") as f:
        conversation_data=json.load(f)
        conversation_data["messages"].append(message)
    with open(file_path, "w") as f:
        json.dump(conversation_data, f, indent=4)