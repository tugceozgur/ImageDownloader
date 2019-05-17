import os 
import requests
import datetime
import configurations as conf
import sys

def logging(log_message):
    with open("logs.txt", "a+") as log:
        log.write("\n" + str(datetime.datetime.now()) + " " + log_message + "\n")

def download_image(image_url,line_number):
    response = requests.get(image_url)
    #get format of image file (jpg, png ..etc)
    image_format = response.headers['Content-Type'].split("/")[1]
    image_name = str(line_number+1)+ "." +image_format
    image_path ="images/" + image_name

    with open(image_path,"wb") as img:
        img.write(response.content)

    image_size = os.path.getsize(image_path)
    assert image_size > conf.min_image_size, ("Image size is too small at " 
                                                + str(line_number) + " \n\tURL is " + line)
    return image_path
      
if __name__ == '__main__':
    directory = "images/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    #takes plaintext file as argument
    with open(sys.argv[1], "r") as urls:
        data = urls.read().splitlines()

        for line_number,line in enumerate(data):
            try:

                assert len(line) > conf.min_line_length, "Image URL is too short" 
                download_image(line,line_number)

            except AssertionError as err_msg:
                logging(str(err_msg) + " at line " + str(line_number))

            except Exception as generic_err:
                logging(str(generic_err))

            