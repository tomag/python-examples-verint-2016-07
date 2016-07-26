"""
Write code to make the following unit test pass
"""
import re
import unittest

class InvalidImageExt(Exception):
    def __init__(self, message):
        self._message = message
    
    def __str__(self):
        return self._message

class ImageFile(object):
    validExtension = "png"
    
    def __init__(self, fileName):
        result = re.search("[a-z,0-9]*.(?P<ext>[a-z,0-9]+)", fileName)
        ext = result.group("ext")
        if not (ext == ImageFile.validExtension):
            raise InvalidImageExt("Extension %s is invalid. Only %s is a valid file extension" % (ext, ImageFile.validExtension))

        self._fileName = fileName

class TestImageFile(unittest.TestCase):
    def test_good_ext(self):
        try:
            img = ImageFile("file.png")
        except InvalidImageExt:
            self.fail("png should be a valid file extension")

    def test_bad_ext(self):
        with self.assertRaises(InvalidImageExt):
            img = ImageFile("file.mp3")

unittest.main()