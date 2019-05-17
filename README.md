Images Download
============

Python Script for 'downloading' images from given plaintext file to the local hard disk!

Install requirements
-----
Make sure you have python3 and pip3 installed.

To install required python packages 
```
pip3 install -r requirements.txt
```
Usage
-----
```
python3 image_downloader.py /path/to/url_links.txt"
```
Remark About Error Handling 
-----
There are more than two error/edge case scenerios but two of them are implemented in this code because of time limitations.
The error/edge scenerios implemented are the followings:
    -First one checks if given url is too short. 
    -Second one checks if image size is too small.
#### NOTE:
There is ``configurations.py`` file that you can specify minimum url length and image size.