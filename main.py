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
    

    #Download Image

    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: "{image_name}" successfully!')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    input_url: str = input("Enter Image url: ")
    input_name: str = input("Enter Image name to save it: ")

    print('Downloading........')
    download_image(input_url, name=input_name, folder='images')
