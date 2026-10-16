from backend.ai.providers.gemini import gemini_request
from backend.ai.providers.groq import groq_request

def ai_request(user_input):
    try:
        response=gemini_request(user_input)
        return response
    except Exception:
        try:
            response=groq_request(user_input)
            return response
        except Exception:
            raise RuntimeError("All AI providers failed.")