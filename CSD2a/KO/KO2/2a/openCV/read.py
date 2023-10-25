
import cv2 as cv

# img = cv.imread('/home/begligow/Documents/CSD2/python_basics/KO/KO2/2a/openCV/foto/tiki.jpg')

# cv.imshow('ti', img)

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
   