from src.llm_calls import call_llm, call_llm_embeddings
from config.llm_config import (
    LLM_API_URL,
    LLM_MODEL,
    EMBEDDINGS_API_URL,
    EMBEDDINGS_MODEL,
)
from src.prompts import (
    IMAGE_DESCRIPTION_PROMPT,
    IMAGE_RENAME_PROMPT,
)


def get_image_description(base64_image):
    messages = [
        {"role": "system", "content": IMAGE_DESCRIPTION_PROMPT},
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                }
            ],
        },
    ]
    output = call_llm(LLM_API_URL, LLM_MODEL, messages)
    return output


def get_image_new_name_from_llm(base64_image):
    messages = [
        {"role": "system", "content": IMAGE_RENAME_PROMPT},
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                }
            ],
        },
    ]
    output = call_llm(LLM_API_URL, LLM_MODEL, messages)
    return output


def get_image_embeddings(base64_image):
    description = get_image_description(base64_image=base64_image)
    description_embeddings = call_llm_embeddings(
        EMBEDDINGS_API_URL, EMBEDDINGS_MODEL, description
    )
    return description_embeddings
