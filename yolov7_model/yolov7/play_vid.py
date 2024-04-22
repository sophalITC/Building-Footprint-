import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', required= True, help='Input video path')

args = vars(ap.parse_args())

cap = cv2.VideoCapture(args['input'])

while True:
    ret, frame = cap.read()

    cv2.imshow('Frame', frame)

    if cv2.waitKey(60) == 27:
        break
cap.release()
cv2.destroyAllWindows()