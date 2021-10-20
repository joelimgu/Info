import cv2

from aruco import ArucoDetector

cam = cv2.VideoCapture(0)
ar = ArucoDetector()

while True:
    _, frame = cam.read()
    cv2.imshow('Input', frame)

    codes = ar.read_frame(frame)

    if len(codes) > 0:
        print("Codes: ", codes)

    c = cv2.waitKey(1)
    if c == 27:
        break

cam.release()
cv2.destroyAllWindows()
