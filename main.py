import os
import requests


def get_extension(image_url: str)-> str | None:
    extension: list[str] = ['.png', '.jpg', '.jpg', '.gif', '.svg']
    for ext in extension:
        if ext in image_url:
            return ext


def download_image(image_url: str, name:str, folder: str = None):
    if ext := get_extension(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name = f'{name}{ext}'
    else:
        raise Exception('Image exxtension could not be found')
    
    #Checking if name already exits
    if os.path.isfile(image_name):
        raise Exception('File name already exits.....')