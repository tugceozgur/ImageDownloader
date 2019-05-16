import requests
with open("url_links.txt", "r") as urls:
    data = urls.read().splitlines()
    for i,line in enumerate(data):
        image_name = str(i).zfill(8)
        urls = open(image_name + ".jpg", "wb")
        urls.write(requests.get(line).content)
    f.close()  

