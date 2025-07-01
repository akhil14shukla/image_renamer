from src.llm_calls import call_llm
from config.llm_config import LLM_API_URL, LLM_MODEL


def get_image_description(base64_image):
    # This function is a placeholder for the actual implementation.
    # It should return a descriptive filename based on the image content.
    # For now, we return a generic name.
    return "image_description"  # Replace with actual logic to get description from LLM


def get_image_new_name_from_llm(base64_image, prompt):
    messages = [
        {"role": "system", "content": prompt},
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
