
import cv2
import sys
import numpy as np
import requests

width = 500
height = 500

# read the image
image = cv2.imread(sys.argv[1])

imgHeight = image.shape[0]
imgWidth = image.shape[1]


# and compute the new height based on the aspect ratio
new_width, new_height = 500 , 500

if imgHeight > imgWidth:
    ratio = height / imgHeight
    new_width = int(imgWidth * ratio)
else:
    ratio = width / imgWidth # (or new_height / height)
    new_height = int(imgHeight * ratio)

dimensions = (new_width, new_height)
resized_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_LINEAR)




backgroundImage = np.zeros((height,width,3), np.uint8)
backgroundImage[:,:] = (26,26,26)

# # I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = resized_image.shape
# print(rows)
roi = backgroundImage[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
resized_imagegray = cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(resized_imagegray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# # Now black-out the area of logo in ROI
backgroundImage_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# # Take only region of logo from logo image.
resized_image_fg = cv2.bitwise_and(resized_image,resized_image,mask = mask)


w1 = resized_image.shape[1]
h1 = resized_image.shape[0]
 
new_w = int((width - w1) / 2)
new_h = int((height - h1) / 2)

# # Put logo in ROI and modify the main image
dst = cv2.add(backgroundImage_bg,resized_image_fg)
backgroundImage[new_h:new_h+h1, new_w:new_w+w1] = dst

# cv2.imshow('res',backgroundImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imwrite(sys.argv[2], backgroundImage)

def getWeather():
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=40.1811&lon=44.5136&appid=8a9528782ecf73a6ab09c90f973c11a4")
    return response.json()


def getImage(weather):
    image_url = 'https://openweathermap.org/img/wn/' + weather['weather'][0]['icon'] + '@2x.png'

    img_data = requests.get(image_url).content
    with open('weaterIcon.jpg', 'wb') as handler:
        handler.write(img_data)
    return 'weaterIcon.jpg'

def getTemp(weather):
    return weather['main']['temp']

