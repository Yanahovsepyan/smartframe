import requests
from delete import removeImage
from downloadimg import getImage

def getJson(url):
    try:
        response = requests.get(url)
        return response.json()
    except:
        return 0

def getdeletedimgs():
    
    deleteImageHost = "http://192.168.0.101:8888/"

    delImgs = dict(getJson(deleteImageHost))
    for img in delImgs:
        removeImage('images/' + delImgs[img])

def getdownloadedimgs():

    imgdownloadHost = "http://192.168.0.121:8888/core.php?getDeletedImages"
     
    downloadimgs = dict(getJson(imgdownloadHost))
    for img in downloadimgs:
        getImage('images/' + downloadimgs[img], downloadimgs[img])
    