import requests



def getImage(url, name):
    
        img_data = requests.get(url).content
        with open(name, 'wb') as handler:
            handler.write(img_data)
       
      
getImage("https://www.freeiconspng.com/thumbs/elephant-png/elephant-png-transparent-1.png", "downloaded.png")
