
import datetime
import cv2
import numpy as np
from math import ceil
import os
import time       
import natsort
from sync import getdeletedimgs, getdownloadedimgs
import weather
import black
from PIL import ImageFont, ImageDraw, Image



weatherObj = weather.getWeather()
if weatherObj:
    weather.getImage(weatherObj)

width = 500 
height = 500 

dst = "./images/"       # Images destination

# Get image names in a list
images = os.listdir(dst)
images = natsort.natsorted(images)   

length = len(images)

result = np.zeros(( width, height ,3), np.uint8)        # Image window of size 
i = 0

a = 1.0     # alpha3
b = 0.0     # beta
black.blackImgToImg(cv2.imread(dst + images[i]))
if weatherObj != 0:
    black.weatherIconToImg(dst + 'cache/new.png')
   
img = cv2.imread(dst + 'cache/new.png')

opacityImg = cv2.imread('images/opacity.png')
# Slide Show Loop

lastTime = time.time()
while(True):
    if(time.time() >  lastTime + 1200):

        getdeletedimgs()
        getdownloadedimgs()
        images = os.listdir(dst)
        images = natsort.natsorted(images)   

        length = len(images)  
        lastTime = time.time()
    if(ceil(a)==0): 
        a = 1.0
        b = 0.0
        i = (i+1)%length    # Getting new image from directory
      
        black.blackImgToImg(cv2.imread(dst + images[i]))
        weatherObj = weather.getWeather()
        if weatherObj != 0:        
            weather.getImage(weatherObj)

        if weatherObj != 0:
            black.weatherIconToImg(dst + 'cache/new.png')
        img = cv2.imread(dst + 'cache/new.png')

    a -= 0.001
    b += 0.001

    # Convert to PIL Image
    cv2_im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im_rgb)

    draw = ImageDraw.Draw(pil_im)

    # Choose a font
    font = ImageFont.truetype("arial.ttf", 25)
    # font = ImageFont.load_default()

    # Draw the text
    draw.text((60, 60), str(datetime.datetime.now().strftime("%H:%M")), fill=(255 ,248 ,220),  font=font)
    if weatherObj != 0:
        draw.text((80,20), str(weather.getTemp(weatherObj)) + '°C', fill=(255 ,248, 220),  font=font)

    # Save the image
    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

    # Image Transition from one to another
    result = cv2.addWeighted(result, a, cv2_im_processed, b, 0)

    cv2.imshow("window", result)
    time.sleep(0.3)
    key = cv2.waitKey(1) & 0xff



    if key==ord('q'):
        break

