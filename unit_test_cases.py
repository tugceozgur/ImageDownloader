from image_downloader import download_image
import unittest
import os.path

class TestImageMethods(unittest.TestCase):

    def test_image_download(self):
        self.urls = ["https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"]
        for i, url in enumerate(self.urls): 
            print(url)
            assert os.path.exists(download_image(url,i)), "Files not downloaded successfully"


if __name__ == '__main__':
    unittest.main()

    