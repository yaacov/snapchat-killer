import cv2
import sys

cascPath = "haarcascade_frontalface_default.xml"
ear_img = cv2.imread("ear.png")
ear_img = cv2.resize(ear_img, (0,0), fx=0.3, fy=0.3)

faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
(x, y, w, h) = 0,0,0,0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # convert image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # look for faces in image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=25,
        minSize=(40, 40),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # if we found a face, remember it
    if len(faces) > 0:
        (x, y, w, h) = faces[0]

    # if we have room for drawing bunny ears, draw them
    if y-ear_img.shape[0] > 0:
        frame[y-ear_img.shape[0]:y, x:x+ear_img.shape[1]] = ear_img
        frame[y-ear_img.shape[0]:y, x+w-ear_img.shape[1]:x+w] = ear_img

    # Display the resulting frame
    cv2.imshow('color', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
