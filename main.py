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


def download_images_from_list(url_list: list[str], folder: Optional[str] = 'images'):
    """
    Downloads images from a list of URLs and saves them with automatically generated names.
    
    Args:
    - url_list (list[str]): A list of image URLs to download.
    - folder (str, optional): The folder to save the images in. Defaults to 'images'. 
    
    """
    for index, image_url in enumerate(url_list):
    # Auto-generate a unique name using the index
        image_name: str = f'image_{index+1}'
        print(f'downloading image {index+1}/{len(url_list)}..........')
        try:
            download_image(image_url, name=image_name, folder=folder)
        except Exception as e:
            print(f'Failed to download {image_url}: {e}')

if __name__=='__main__':
    #LIST OF IMAGE URLs TO DOWNLOAD
    image_urls = ['https://media.istockphoto.com/id/1415551608/photo/happy-middle-aged-couple-together-on-a-road-trip-caucasian-woman-and-man-having-fun-on.jpg?s=612x612&w=0&k=20&c=LdKfyamobdI069sxBRgpavMNJyQWXsmbWIqPqLhy4uE=',
                  'https://media.istockphoto.com/id/1176439818/photo/making-a-memory.jpg?s=1024x1024&w=is&k=20&c=Yk_c7POcnawBoIHQEMHu9o2tRsPvvzYwL_XJuqcv5Sg=',
                  'https://media.istockphoto.com/id/1170543777/photo/enjoying-the-view.jpg?s=1024x1024&w=is&k=20&c=-6zMlhf13ugESHTR2i-hUkgs5KxpRhIOLJ3H-uU-hqs=',
                  'https://media.istockphoto.com/id/1707927462/photo/road-trip-romance.jpg?s=1024x1024&w=is&k=20&c=iisCxC6I2IwwRF84Tu9_JvDXHmLY5rFMayGx8EzfMuc=',
                  'https://media.istockphoto.com/id/2161113463/photo/aerial-photography-of-modern-city-skyline.jpg?s=1024x1024&w=is&k=20&c=nl55aVk3g3tHMgiEGGNSMZoRImvmGenkhuxTwEPLk64='
                  ]
# if __name__ == '__main__':
    # input_url: str = input("Enter Image url: ")
    # input_name: str = input("Enter Image name to save it: ")

    # print('Downloading........')
    # download_image(input_url, name=input_name, folder='images')

    print('Starting batch download...')
    download_images_from_list(image_urls)