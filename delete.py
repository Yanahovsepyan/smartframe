import os


def removeImage(name):
    try: 
        os.remove(name)
    except: pass 
    
# removeImage("download.png") 