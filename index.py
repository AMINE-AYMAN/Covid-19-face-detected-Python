import numpy as np
import cv2
from math import sqrt

cap = cv2.VideoCapture("videos/walking.avi")
body_classifer = cv2.CascadeClassifier("haarcascades/haarcascade_fullbody.xml")
while cap.isOpened():
    ret, frame = cap.read()
    bodys = body_classifer.detectMultiScale(frame)
    for(x, y, w, h) in bodys:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        xp = (x+(x+w))/2
        yp = (y+(y+h))/2
        np_array2 = ([xp, yp])
        np_array2.append(np_array2)
        for a in np_array2:
            for b in np_array2:
                c = sqrt((a[0]-b[0])*2 + (a[1]-b[1])*2)
                d = str(c)
                cv2.putText(frame, d, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
                if c < 200:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    if ret == True:
        cv2.imshow("Walking", frame)
        key = cv2.waitKey(40)
        if key == 27:
            break
    else:
        break
cv2.destroyAllWindows()
cap.release()