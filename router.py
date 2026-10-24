from backend.ai.providers.gemini import gemini_request
from backend.ai.providers.groq import groq_request

def ai_request(user_input, retrieved_relevent_history):
    try:
        response=gemini_request(user_input, retrieved_relevent_history)
        return response
    except Exception:
        try:
            response=groq_request(user_input, retrieved_relevent_history)
            return response
        except Exception:
            raise RuntimeError("All AI providers failed.")