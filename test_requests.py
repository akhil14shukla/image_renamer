import requests

import base64

base64_image = base64.b64encode(
    open("/Users/akhil/Wallpapers/pexels-sebastian-312105.jpg", "rb").read()
).decode("utf-8")

response = requests.post(
    url="http://192.168.68.110:1234/v1/chat/completions",
    headers={"Content-Type": "application/json"},
    json={
        "model": "google/gemma-3-12b",
        "messages": [
            {
                "role": "system",
                "content": "Describe the content of this image in 3-4 lines, be detailed but concise.",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    }
                ],
            },
        ],
    },
)
response.raise_for_status()
data = response.json()
print(data)
