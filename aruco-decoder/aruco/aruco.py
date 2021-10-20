import cv2
from numpy import ndarray


class ArucoDetector:
    def __init__(self):
        """A class to detect Aruco code from an image"""
        self.type = cv2.aruco.DICT_4X4_50

    def read_image(self, image_path):
        """
        Read aruco codes from an image and return values inside

        Args:
            image_path (str): Path to the image

        Returns:
           (ndarray): Values read from the image
        """
        # load the input image from disk
        image = cv2.imread(image_path)

        # load the ArUCo dictionary, grab the ArUCo parameters, and detect the markers
        aruco_dict = cv2.aruco.Dictionary_get(self.type)
        aruco_params = cv2.aruco.DetectorParameters_create()
        corners, ids, rejected = cv2.aruco.detectMarkers(image, aruco_dict, parameters=aruco_params)

        if ids is None:
            return []
        return ids

    def read_frame(self, frame):
        """
        Read aruco codes from a frame and returns values inside

        Args:
            frame (ndarray): Frame to read

        Returns:
           (ndarray): Values read from the frame
        """
        aruco_dict = cv2.aruco.Dictionary_get(self.type)
        aruco_params = cv2.aruco.DetectorParameters_create()
        corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=aruco_params)

        if ids is None:
            return []
        return ids
