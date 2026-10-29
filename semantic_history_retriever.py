import json
from pathlib import Path
import numpy
from backend.history.semantic_search.router_of_semantic_search import create_user_embedding

list_of_json=[]
dictionaries_in_list_in_dictionary=dict()
semantic_sessions_dir=Path(__file__).parent.parent/"semantic_sessions"
semantic_session_files=semantic_sessions_dir.iterdir()
for i in semantic_session_files:
    if(i.suffix==".json"):
        list_of_json.append(i)
sorted_session=sorted(
    list_of_json,
    key=lambda i: i.stat().st_mtime,
    reverse=True
)

for i in sorted_session:
    with open(i, "r") as f:
        session_content=json.load(f)
        list_of_dictionaries=session_content["messages"]
        dictionaries_in_list_in_dictionary[i.name]=list_of_dictionaries
    
def search_semantic_history(user_input):
    similarity_scores=[]
    user_input_embedding=create_user_embedding(user_input)
    for i in dictionaries_in_list_in_dictionary:
        list_of_messages=dictionaries_in_list_in_dictionary[i]
        for position, message in enumerate(list_of_messages):
            embedding=message["content"]
            if(embedding==None):
                continue
            else:
                user_input_embedding=numpy.array(user_input_embedding)
                saved_message_embedding=numpy.array(embedding)
                denominator=numpy.linalg.norm(user_input_embedding) * numpy.linalg.norm(saved_message_embedding)
                if(denominator==0):
                    continue
                similarity=numpy.dot(user_input_embedding, saved_message_embedding)/denominator
                result={
                    "filename": i,
                    "position": position,
                    "similarity": similarity
                }
                similarity_scores.append(result)
    sorted_similarity_scores=sorted(
        similarity_scores,
        key=lambda i: i["similarity"],
        reverse=True
    )
    return sorted_similarity_scores