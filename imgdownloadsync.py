import requests
from delete import removeImage

imgHost = "http://192.168.0.101:8888/"

def getJson(url):
    try:
        response = requests.get(url)
        return response.json()
    except:
        return 0