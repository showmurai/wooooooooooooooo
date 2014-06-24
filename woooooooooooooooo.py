# -*- coding: utf-8 -*-


import cv2
import video
import sys


cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"


if __name__ == '__main__':
    print __doc__

    try:
        fn = sys.argv[1]
    except:
        fn = 0

    def nothing(*arg):
        pass

    color = (255, 255, 255)
    cv2.namedWindow('Wooooooooooooo')

    cap = video.create_capture(fn)
    while True:
        flag, image = cap.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascade_path)
        facerect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

        if len(facerect) > 0:
            for rect in facerect:
                cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

        ch = cv2.waitKey(5)
        if ch == 27:
            break
        cv2.imshow('Wooooooooooooo', image)
    cv2.destroyAllWindows()
