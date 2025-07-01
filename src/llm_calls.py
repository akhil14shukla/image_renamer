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


def call_llm_embeddings(EMBEDDINGS_API_URL, EMBEDDINGS_MODEL, messages):
    """
    Call the LLM API with the provided JSON data.
    """
    response = requests.post(
        url=EMBEDDINGS_API_URL,
        headers={"Content-Type": "application/json"},
        json={
            "model": EMBEDDINGS_MODEL,
            "input": messages,
        },
    )
    response.raise_for_status()
    data = response.json()
    # print(data)
    # Extract the content from the LLM response
    return data["data"][0]["embedding"]
