import time
import shutil
import os
import datetime
from itertools import cycle
from picamera import PiCamera
from image_analyser import cat_in_pic

camera = PiCamera()
temp_filenames = cycle([f'/home/pi/Desktop/image_{i}.jpg' for i in range(50)])


while True:
   
   # Define where image will be saved and timestamp
    temp_image_location = next(temp_filenames)
    timestamp = datetime.datetime.now().strftime('%Y_%m_%d %H_%M_%S')
    
    # Start camera to adjust to light during 2 seconds
    camera.start_preview(temp_image_location)
    sleep(2)

    # Take the picture and stop the preview
    camera.capture()
    camera.stop_preview()

    if cat_in_pic(temp_image_location):
        shutil.move(src=temp_image_location, dst= f'/home/pi/Desktop/cats/{timestamp}.jpg')
    else:
        os.remove(temp_image_location)

