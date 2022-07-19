import os


def checkForDelete():
    return ["gduged.png","ufrfr.png"]

imagesToDelete = checkForDelete()
for img in imagesToDelete:
    def removeImage(name):
    try: 
        os.remove(name)
    except: pass 

checkForDelete(img)     

