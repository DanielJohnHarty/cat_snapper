import boto3
import os

client=boto3.client('rekognition')

def is_valid_image_filetype(image_pth):

    compatible_image_types = ['jpg','jpeg','png']
    
    image_filetype = image_pth.split('.')[-1]

    return image_filetype in compatible_image_types


def item_in_pic(search_string=None, image_pth=None, client=client)->bool:
    """
    search_string: The item you're searching for in the picture e.g. 'cat' or 'car'
    image_pth: The absolute path to the local image e.g. '/home/username/Desktop/myimage.jpeg'
    client: An initiated client to interact with the google api. Credentials are automatically loaded
            from the /home/pi/.aws/credentials file


    Loads an image, whose path is passed as a parameter and checks sends it to google
    rekognition looking for the search string object. E.g is a 'cat' in the image -> True/False 
    """

    search_string_ok = search_string is not None
    image_pth_ok = image_pth is not None and is_valid_image_filetype(image_pth)
    
    if search_string_ok and image_pth_ok:

        with open(image_pth, 'rb') as image:
            response = client.detect_labels(Image={'Bytes': image.read()})

        item_in_pic = \
            search_string.lower() in [label['Name'].lower() for label in response['Labels']]
        
        return item_in_pic