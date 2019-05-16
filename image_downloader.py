import os 
import requests
import datetime

def logging(line_number):
    print(str(datetime.datetime.now()) + " invalid address in "  + str(line_number) +" line.")

with open("url_links.txt", "r") as urls:
    data = urls.read().splitlines()
    for i,line in enumerate(data):
        if len(line) < 5:
            logging(i)
            continue
        image_name = os.path.basename(line)
        image = open("images/" + image_name, "wb")
        image.write(requests.get(line).content)
    image.close()  

