import requests


def call_llm(LLM_API_URL, LLM_MODEL, messages):
    """
    Call the LLM API with the provided JSON data.
    """
    response = requests.post(
        url=LLM_API_URL,
        headers={"Content-Type": "application/json"},
        json={
            "model": LLM_MODEL,
            "messages": messages,
        },
    )
    response.raise_for_status()
    data = response.json()
    # Extract the content from the LLM response
    return data["choices"][0]["message"]["content"].strip()
