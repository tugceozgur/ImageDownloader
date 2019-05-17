from image_downloader import download_image
import unittest
import os

class TestImageMethods(unittest.TestCase):
    
    def setUp(self):
        self.image_path = "/tmp/images/"
        os.system("mkdir -p " + self.image_path)

    def test_image_download(self):
        self.urls = ["https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"]
        for i, url in enumerate(self.urls):
            assert os.path.isfile(download_image(url,i,self.image_path)), "Files not downloaded successfully"


if __name__ == '__main__':
    unittest.main()

    