from api_keys import jina_api_key
import requests

def _embed_text(text):
    url="https://api.jina.ai/v1/embeddings"

    headers={
        "Authorization": f"Bearer {jina_api_key}",
        "Content-Type": "application/json"
    }

    data={
        "model": "jina-embeddings-v3",
        "task": "text-matching",
        "input": [text]
    }

    response=requests.post(
        url,
        headers=headers,
        json=data,
        timeout=15
    )

    response.raise_for_status()
    result=response.json()
    embedding=result["data"][0]["embedding"]
    return embedding

def embed_user_input(user_input):
    return _embed_text(user_input)

def embed_assistant_response(response):
    return _embed_text(response)