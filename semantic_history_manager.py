import json
from pathlib import Path


def new_semantic_conversation_file(file_path):
    semantic_sessions_dir=Path(__file__).parent.parent/"semantic_sessions"
    file_name=Path(file_path).name
    semantic_session=file_name.replace("session", "semantic")
    semantic_file_path=semantic_sessions_dir/f"{semantic_session}"

    semantic_sessions_dir.mkdir(parents=True, exist_ok=True)
    with open(semantic_file_path, "x") as f:
        json.dump({"messages": []}, f, indent=4)
    return semantic_file_path

def save_semantic_message(file_path, message):
    with open(file_path, "r") as f:
        conversation_data_of_semantic_files=json.load(f)
        conversation_data_of_semantic_files["messages"].append(message)
    with open(file_path, "w") as f:
        json.dump(conversation_data_of_semantic_files, f, indent=4)
