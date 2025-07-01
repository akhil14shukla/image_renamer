## Main script to rename images in a directory using LLM-generated names

from src.utils import get_image_files, image_to_bytes
from src.image_functions import get_image_new_name_from_llm, get_image_embeddings
import os


def rename_images_in_directory(directory):
    image_files = get_image_files(directory)
    for filename in image_files:
        file_path = os.path.join(directory, filename)
        image_bytes = image_to_bytes(file_path)
        try:
            new_name = get_image_new_name_from_llm(image_bytes)
            ext = os.path.splitext(filename)[1].lower()
            new_filename = f"{new_name}{ext}"
            new_path = os.path.join(directory, new_filename)
            if new_filename != filename:
                os.rename(file_path, new_path)
                print(f"Renamed '{filename}' to '{new_filename}'")
            else:
                print(f"No change for '{filename}'")
        except Exception as e:
            print(f"Failed to rename '{filename}': {e}")


def cluster_images_by_embeddings(directory):
    from sklearn.cluster import KMeans
    import numpy as np

    image_files = get_image_files(directory)
    embeddings = []

    for filename in image_files:
        file_path = os.path.join(directory, filename)
        image_bytes = image_to_bytes(file_path)
        embedding = get_image_embeddings(image_bytes)
        embeddings.append(embedding)

    embeddings = np.array(embeddings)
    kmeans = KMeans(n_clusters=2)  # Adjust number of clusters as needed
    kmeans.fit(embeddings)

    for i, filename in enumerate(image_files):
        cluster_label = kmeans.labels_[i]
        print(f"Image '{filename}' is in cluster {cluster_label}")
