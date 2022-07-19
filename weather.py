import requests
import urllib.request
from PIL import Image



def getWeather():
    try:
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=40.1811&lon=44.5136&appid=8a9528782ecf73a6ab09c90f973c11a4")
        return response.json()
    except:
        return 0

def getImage(weather):
    try:
        image_url = 'https://openweathermap.org/img/wn/' + weather['weather'][0]['icon'] + '@2x.png'
     
        urllib.request.urlretrieve(image_url, "weaterIcon.png")
        
        png = Image.open(r'weaterIcon.png')
        png.load() # required for png.split()

        background = Image.new("RGB", png.size, (255, 255, 0))
        background.paste(png, mask=png.split()[3]) # 3 is the alpha channel

        background.save('weaterIcon.jpg', 'JPEG', quality=80)
        return "weaterIcon.jpg"
    except:
        return 0
def getTemp(weather):
    try:
        return weather['main']['temp']
    except:
        return 0

weather = getWeather()
print(getImage(weather))

