import os 
import requests
import datetime

def logging(log_message):
    with open("logs.txt", "a+") as log:
        log.write(str(datetime.datetime.now()) + " " + log_message + "\n")

with open("url_links.txt", "r") as urls:
    data = urls.read().splitlines()
    for line_number,line in enumerate(data):
        try:
            assert len(line) > 5, "Image URL is too short"
            image_name = os.path.basename(line)
            image = open("images/" + image_name, "wb")
            image.write(requests.get(line).content)
        except AssertionError as err_msg:
            logging(str(err_msg) + " at line " + str(line_number))
        except Exception as generic_err:
            logging(str(generic_err))
    image.close()  

