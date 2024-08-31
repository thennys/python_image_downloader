import os
import requests
from typing import Optional


def get_extension(image_url: str)-> str | None:
    extension: list[str] = ['.png', '.jpg', '.jpg', '.gif', '.svg']
    # Convert URL to lowercase to handle case insensitivity
    image_url = image_url.lower()
    for ext in extension:
        if ext in image_url:
            return ext
        
    # for ext in extensions:
    #     if image_url.endswith(ext) or f'{ext}?' in image_url:  # Check if URL ends with an extension or has a query parameter.
    #         return ext


def download_image(image_url: str, name:str, folder:Optional[str] = None):
    #folder (str, optional): The folder to save the image in. Defaults to None.
    
    if ext := get_extension(image_url):
        if folder:
            # Ensure folder exists
            os.makedirs(folder, exist_ok=True)
            image_name = os.path.join(folder, f'{name}{ext}')
            #image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name = f'{name}{ext}'

                # Prepare the folder and filename
    
    else:
        raise Exception('Image extension could not be found')
    
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
