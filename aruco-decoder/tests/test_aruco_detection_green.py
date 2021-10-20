import os
import unittest

from aruco import ArucoDetector


class TestArucoDetectionGreen(unittest.TestCase):

    ar = ArucoDetector()

    GREEN = 36

    def test_green(self):
        result = self.ar.read_image(os.path.abspath("./datasets/green.jpg"))
        self.assertEqual(self.GREEN, result)

    def test_green_tilted_r(self):
        result = self.ar.read_image(os.path.abspath("./datasets/green-tilted-r.jpg"))
        self.assertEqual(self.GREEN, result)

    def test_green_reverse(self):
        result = self.ar.read_image(os.path.abspath("./datasets/green-reverse.jpg"))
        self.assertEqual(self.GREEN, result)

    def test_green_tilted_l(self):
        result = self.ar.read_image(os.path.abspath("./datasets/green-tilted-l.jpg"))
        self.assertEqual(self.GREEN, result)
