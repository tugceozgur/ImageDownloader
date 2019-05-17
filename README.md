Image Downloader
============

Python Script for 'downloading' images from given plaintext file to the local hard disk!

The code expects a text file that contains image urls in its each line and downloads these images to images folder. 

Install requirements
-----
Make sure you have python3 and pip3 installed.

To install required python packages 
```
pip3 install -r requirements.txt
```
Usage
-----
execute the ``image_downloader.py`` using python3 with path to text file containing the image urls as an argument. Images file will be created inside of ``./images/``

```
python3 image_downloader.py /path/to/url_links.txt
```
In case if you want images to be created in a certain path add an additional argument

```
python3 image_downloader.py /path/to/url_links.txt /path/to/images/
```
#### NOTE:
trailing '/' is required

To run unit test, use the following:

```
python3 unit_test_cases.py
```
Remark About Error Handling 
-----
There are more than two error/edge case scenerios but two of them are implemented in this code because of time limitations.

The error/edge scenerios implemented are the followings:

-First one checks if given url is too short.

-Second one checks if image size is too small.
#### NOTE:
There is ``configurations.py`` file that you can specify minimum url length and image size.