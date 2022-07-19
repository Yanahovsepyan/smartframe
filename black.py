import cv2
from PIL import Image

def blackImgToImg(img):
   
    """
        Put black image , which helps to show time&number  
    """
    watermark = cv2.imread("black.png")




    percent_of_scaling = 100

    new_width = int(img.shape[1] * percent_of_scaling/100)

    new_height = int(img.shape[0] * percent_of_scaling/100)

    new_dim = (new_width, new_height)

    resized_img = cv2.resize(img, new_dim, interpolation=cv2.INTER_AREA)





    wm_scale = 40

    wm_width = int(watermark.shape[1] * wm_scale/100)

    wm_height = int(watermark.shape[0] * wm_scale/100)

    wm_dim = (wm_width, wm_height)




    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)




    h_img, w_img, _ = resized_img.shape

    h_wm, w_wm, _ = resized_wm.shape

    top_y = 0

    left_x = 1

    bottom_y = top_y + h_wm

    right_x = left_x + w_wm





    roi = resized_img[top_y:bottom_y, left_x:right_x]

    result = cv2.addWeighted(roi, 0.7, resized_wm, 1, 1)

    resized_img[top_y:bottom_y, left_x:right_x] = result
    cv2.imwrite("images/cache/new.png", resized_img)






    # Weater icon 
def weatherIconToImg(img):
   
  

    
  # Front Image
  filename = 'weaterIcon.png'
    
  # Open Front Image
  frontImage = Image.open(filename)
    
  # Open Background Image
  background = Image.open(img)    
  # Convert image to RGBA
  frontImage = frontImage.convert("RGBA")
    
  # Convert image to RGBA
  background = background.convert("RGBA")
    
  # Calculate width to be at the center
  width = -13
  height = -13
    
    
  # Paste the frontImage at (width, height)
  background.paste(frontImage, (width, height), frontImage)
    
  # Save this image
  background.save("images/cache/new.png", format="png")
