import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from djitellopy import Tello
import numpy as np
tello = Tello()
tello.connect()
tello.streamon()
def get_resized_frame(w=640,h=480):
    return cv2.resize(tello.get_frame_read().frame,(w,h))
while True:
    img = get_resized_frame()
    bbox, label, conf = cv.detect_common_objects(img)
    output_image = draw_bbox(img, bbox, label, conf)
    bat = "Battery: {}%".format(tello.get_battery())
    cv2.putText(output_image, bat, (5, 480-5),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    temp = "Temperature: {}%C".format(tello.get_temperature())
    cv2.putText(output_image, temp, (5, 480-25),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Image", output_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
tello.streamoff()
cv2.destroyAllWindows()
