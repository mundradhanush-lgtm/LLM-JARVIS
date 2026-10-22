from pathlib import Path
import json
import string

dictionaries_in_list_in_dictionary=dict()
list_of_json=[]
sessions_dir=Path(__file__).parent/"sessions"
session_files=sessions_dir.iterdir()
for i in session_files:
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

def command_normalization(user_input):
    user_input=user_input.lower()
    user_input=user_input.translate(str.maketrans("", "", string.punctuation))
    command_word_list=user_input.split()
    stop_word_list=["a", "an", "the", "this", "that", "these", "those", "some", "any", "each", "every", "all", "another", "such", "i", "me", "my", "mine", "we", "us", "our", "ours", "you", "your", "yours", "he", "him", "his", "she", "her", "hers", "it", "its", "they", "them", "their", "theirs", "who", "whom", "whose", "am", "is", "are", "was", "were", "be", "been", "being", "do", "does", "did", "have", "has", "had", "can", "could", "may", "might", "must", "shall", "should", "will", "would", "about", "above", "across", "after", "against", "along", "among", "around", "at", "before", "behind", "below", "beneath", "beside", "between", "by", "down", "during", "for", "from", "in", "inside", "into", "near", "of", "off", "on", "onto", "out", "outside", "over", "through", "to", "toward", "under", "until", "up", "upon", "with", "within", "without", "and", "but", "or", "nor", "so", "yet", "because", "although", "though", "while", "whereas", "unless", "whether", "if", "what", "when", "where", "which", "who", "whom", "whose", "why", "how", "just", "very", "really", "quite", "rather", "too", "also", "only", "even", "still", "already", "again", "ever", "never", "always", "often", "sometimes", "usually", "maybe", "perhaps", "please", "kindly"]
    keyword_list=[]
    for i in command_word_list:
        if(i not in stop_word_list):
            keyword_list.append(i)
    return keyword_list

def search_history(user_input):
    keywords=command_normalization(user_input)
    relevency_dictionary=dict()
    key_counter=0
    for file_names in dictionaries_in_list_in_dictionary.keys():
        message_list=dictionaries_in_list_in_dictionary[file_names]
        for conversation_dictionary in message_list:
            content=conversation_dictionary["content"]
            keywords_of_the_content=command_normalization(content)
            score_variable=0
            for i in keywords:
                if(i in keywords_of_the_content):
                    score_variable+=1
                else:
                    continue
            if(score_variable>0):
                value_tuple=(conversation_dictionary, score_variable)
                relevency_dictionary[key_counter]=value_tuple
                key_counter+=1
            else:
                continue

    sorted_dictionaries_by_relevence_score=sorted(
        relevency_dictionary.values(),
        key=lambda value_tuple: value_tuple[1],
        reverse=True
    )