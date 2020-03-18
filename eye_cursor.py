import numpy as np
import cv2

cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )
fps =  cap.get(cv2.CAP_PROP_FPS)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    #ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    #ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
    #ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)
    #ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO_INV)
    ret,thresh1 = cv2.threshold(gray,100,255,cv2.THRESH_TOZERO)
    ret,thresh1 = cv2.threshold(thresh1,127,255,cv2.THRESH_BINARY)

    roi = thresh1[0: 100, 200: 400  ]
    #roi = thresh1[0: int(width), 0: int(height)]

    # Display the resulting frame
    cv2.imshow('frame',roi)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
