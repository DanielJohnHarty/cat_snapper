import time
import shutil
import os
import datetime
from itertools import cycle
from picamera import PiCamera
from image_analyser import item_in_pic


camera = PiCamera()
temp_filenames = cycle([f'/home/pi/Desktop/cats/temp_images/image_{i}.jpg' for i in range(5)])
cat_pic_storage_location = '/home/pi/Desktop/cats'

def take_pic(save_location):
    # Start camera to adjust to light during 2 seconds
    camera.start_preview(save_location)
    sleep(2)

    # Take the picture and stop the preview
    camera.capture()
    camera.stop_preview()


def check_for_cats():
   # Define where image will be saved and timestamp
    temp_image_location = next(temp_filenames)
        
    # Take the picture and save to disk
    take_pic(temp_image_location)

    # Check for cats
    cat_in_pic = item_in_pic(search_string='cat', image_pth=temp_image_location)

    if cat_in_pic:

        # This function takes the temp_image_location and moves the file to the permanent storage location
        permanently_save_image(temp_image_location, cat_pic_storage_location)
        print(f"Cat spotted at {datetime.datetime.now().strftime('%Y_%m_%d %H_%M_%S')}!")

    else:
        # Otherwise we just remove it; We only care about cat pics.
        os.remove(temp_image_location)


def permanently_save_image(src_path, dest_path):
    
    # Create permanenet filename using timestamp and target dir location
    timestamp = datetime.datetime.now().strftime('%Y_%m_%d %H_%M_%S')
    filename = os.path.basename(src_path)
    permanent_filename = timestamp+filename.split('.')[-1]
    
    # Then store on disk by moving
    shutil.move(src=src_path, \
                dst= os.path.join(dest_path, permanent_filename))


if __name__ == '__main__':
    
    while True:
        check_for_cats()
        time.sleep(6)


