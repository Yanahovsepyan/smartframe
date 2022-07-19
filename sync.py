import requests
from delete import removeImage

deleteImageHost = "http://192.168.0.101:8888/"

def getJson(url):
    try:
        response = requests.get(url)
        return response.json()
    except:
        return 0

delImgs = dict(getJson(deleteImageHost))
for img in delImgs:
    # print('images/' + delImgs[img])
    removeImage('images/' + delImgs[img])
    
