import requests
import os
import glob
from concurrent.futures import ThreadPoolExecutor
from requests import Response
from constants import (
    PIXABAY_API_KEY,
    PIXABAY_URL,
    ROOT_FOLDER,
)


def prepare_infra():
    '''
    Эта функция сначала проверяет, существует ли директория, которая находится в переменной ROOT_FOLDER.
    Если да, то в переменную files_to_delete мы помещаем список  всех файлов, которые находятся в папке ROOT_FOLDER.
    Далее мы удаляем все файлы из этого списка.
    Далее мы создаем эту папку и говорим программе: не ругайся, если папка уже есть.
    '''
    if os.path.exists(ROOT_FOLDER):
        files_to_delete = glob.glob(f"{ROOT_FOLDER}/*")
        [os.remove(f) for f in files_to_delete]

    os.makedirs(ROOT_FOLDER, exist_ok=True)


def download_video(video_info):
    filename = f"{ROOT_FOLDER}/{video_info['filename']}"
    res: Response = requests.get(url=video_info['video_url'], stream=True)

    if res.status_code == requests.codes.ok:
        with open(filename, "wb") as file:
            for chunk in res.iter_content(chunk_size=8192):
                file.write(chunk)


def search_prepare_videos(pattern, amount):
    index_urls = {}
    params = {"key": PIXABAY_API_KEY, "q": pattern}
    res = requests.get(url=PIXABAY_URL, params=params).json()
    print(f"Pixabay Videos Result:\n{res}")
    # hits -> [{'videos': {"large": {"url": "video.mp4 }, ...]

    for idx in range(amount):
        video_url = res['hits'][idx]['videos']['large']['url']
        index_urls[idx] = {
            "video_url": video_url,
            'filename': f'{pattern}_{idx}.mp4'
        }
    print(f"Video files to download:\n {index_urls}")

    with ThreadPoolExecutor(max_workers=len(index_urls)) as executor:
        for idx, video_info in index_urls.items():
            executor.submit(download_video, video_info=video_info)


# Entry point
video_theme: str = input("Enter Video Theme: ")
video_amount = int(input("How many video files download?:"))
prepare_infra()
search_prepare_videos(video_theme, video_amount)
