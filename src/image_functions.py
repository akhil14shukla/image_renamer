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
from src.utils import (
    get_image_files,
    image_to_bytes,
    cosine_similarity,
    get_image_cache_key,
)
import os


def get_image_description(base64_image):
    # using caching to avoid repeated calls to the LLM for the same image
    # create a cache dictionary if it doesn't exist
    os.makedirs("cache", exist_ok=True)
    cache_file = os.path.join("cache", f"{get_image_cache_key(base64_image)}_desc")
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f:
            return f.read()
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
    # Save the output to a cache file
    with open(cache_file, "w") as f:
        f.write(output)
    print(f"Image description saved to {cache_file}")
    return output


def get_image_new_name_from_llm(base64_image):
    # using caching to avoid repeated calls to the LLM for the same image
    # create a cache dictionary if it doesn't exist
    os.makedirs("cache", exist_ok=True)
    cache_file = os.path.join("cache", f"{get_image_cache_key(base64_image)}_name")
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f:
            return f.read()
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
    # Save the output to a cache file
    with open(cache_file, "w") as f:
        f.write(output)
    print(f"Image new name saved to {cache_file}")
    return output


def get_image_embeddings(base64_image):
    description = get_image_description(base64_image=base64_image)
    description_embeddings = call_llm_embeddings(
        EMBEDDINGS_API_URL, EMBEDDINGS_MODEL, description
    )
    return description_embeddings


def cluster_images_by_embeddings(folder_path):
    """
    Clusters images based on their embeddings using hdbscan
    :param base64_images: List of base64 encoded image strings.
    :return: List of cluster labels for each image.
    """

    image_files = get_image_files(folder_path)
    base64_images = []
    for image in image_files:
        file_path = os.path.join(folder_path, image)
        base64_images.append(image_to_bytes(file_path))
    embeddings = [get_image_embeddings(b64_image) for b64_image in base64_images]

    # Here you would implement the clustering logic using hdbscan or any other method
    import hdbscan

    clusterer = hdbscan.HDBSCAN(min_cluster_size=2, metric=cosine_similarity)
    clusterer.fit(embeddings)
    labels = clusterer.labels_
    print(f"Cluster labels: {labels}")
    return embeddings  # Placeholder for clustering logic
