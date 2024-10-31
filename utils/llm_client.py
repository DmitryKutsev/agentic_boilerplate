import os

from langsmith.wrappers import wrap_openai
from together import Together

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
CURR_LLM_MODEL = os.getenv("CURR_LLM_MODEL")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")


def llm_pipeline(user_input: str) -> str:
    together_client = (
        wrap_openai(Together(api_key=TOGETHER_API_KEY))
        if LANGCHAIN_TRACING_V2
        else Together(api_key=TOGETHER_API_KEY)
    )
    result = together_client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}], model=CURR_LLM_MODEL
    )
    return result.choices[0].message.content
