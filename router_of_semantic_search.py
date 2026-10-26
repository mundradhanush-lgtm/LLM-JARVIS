from backend.history.semantic_search.providers.jina import embed_user_input, embed_assistant_response

def create_user_embedding(user_input):
    return embed_user_input(user_input)

def create_assistant_embedding(response):
    return embed_assistant_response(response)