import os
import unittest

from aruco import ArucoDetector


class TestArucoDetectionRed(unittest.TestCase):

    ar = ArucoDetector()

    RED = 47

    def test_red(self):
        result = self.ar.read_image(os.path.abspath("./datasets/red.jpg"))
        self.assertEqual(self.RED, result)

    def test_red_tilted_r(self):
        result = self.ar.read_image(os.path.abspath("./datasets/red-tilted-r.jpg"))
        self.assertEqual(self.RED, result)

    def test_red_reverse(self):
        result = self.ar.read_image(os.path.abspath("./datasets/red-reverse.jpg"))
        self.assertEqual(self.RED, result)

    def test_red_tilted_l(self):
        result = self.ar.read_image(os.path.abspath("./datasets/red-tilted-l.jpg"))
        self.assertEqual(self.RED, result)
