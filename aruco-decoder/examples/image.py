import os
from aruco import ArucoDetector

ar = ArucoDetector()
img = os.path.abspath("../datasets/red.jpg")

print(ar.read_image(img))
