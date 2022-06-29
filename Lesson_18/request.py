import requests
import os
from io import BytesIO
from PIL import Image


HTTPBIN = 'https://httpbin.org/'
IMAGE_ENDPOINT = "image/jpeg"
IMAGE_URL = os.path.join(HTTPBIN, IMAGE_ENDPOINT)


def download_images():
    res = requests.get(IMAGE_URL)
    with open("test_img.jpg", 'wb') as img:
        img.write(res.content)
    img = Image.open(BytesIO(res.content))
    img.save("test_img.jpg")
    return res


# download_images()
image_res = download_images()
