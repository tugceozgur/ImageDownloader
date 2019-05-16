import os 
import requests
with open("url_links.txt", "r") as urls:
    data = urls.read().splitlines()
    for i,line in enumerate(data):
        image_name = os.path.basename(line)
        image = open(image_name, "wb")
        image.write(requests.get(line).content)
    image.close()  

