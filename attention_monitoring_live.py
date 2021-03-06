from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import os
import cv2
import atten_class.attention_calc as tp

# c = tp.attention()
obj = tp.facial_point_operation()
obj.init()


def atten(frame):
    str = obj.loop_operation(frame)
    if str == 0:
        return "attentive"

    elif str == 1:
        return "non_attentive_eyes_closed"
    elif str == 2:
        return "non_attentive_open_mouth"
    else:
        return "not_dected"


ap = argparse.ArgumentParser()

# constructing argument to pass weights and deploy files for caffe
# model

ap.add_argument("-p", "--prototext", required=True, help="path to .deploy file")

ap.add_argument("-m", "--model", required="True", help="path to .caffe file")
ap.add_argument("-c", "--conf", default=0.5, type=float, help="threshold value")

# camera ID for local webcam ID is 0 for other cam try numbers 1,2.. onwards
# ap.add_argument("-v", "--camera", default=0, type=int, help="Camera ID")
ap.add_argument("-v", "--camera", default=0, type=int, help="path to camera location")

args = vars(ap.parse_args())

# load model from .caffe file available in same dir

net = cv2.dnn.readNetFromCaffe(args["prototext"], args["model"])

vs = VideoStream(src=args["camera"]).start()

while True:

    window = vs.read()
    window = imutils.resize(window, width=500)

    (height, width) = window.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(window, (300, 300)), 1.0, (300, 300), (0, 0, 255))

    net.setInput(blob)
    detections = net.forward()

    for i in range(0, detections.shape[2]):

        conf = detections[0, 0, i, 2]
        # predefined threshold 0.5
        if conf < args["conf"]:
            continue
        # box = detections[0, 0, i, 3:7] * np.array(width, height, width, height)
        box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])

        (sX, sY, eX, eY) = box.astype("int")

        y = sY - 10 if sY - 10 > 10 else sY + 10
        frame = window[sY - 10:eY + 10, sX - 10:eX + 10]
        # cv2.imshow("frame", frame)
        text = "{:.2f}%".format(conf * 100) + atten(frame)

        cv2.rectangle(window, (sX, sY), (eX, eY), (0, 255, 0), 2)

        cv2.putText(window, text, (sX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)

    cv2.imshow("Window", window)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()
print("code reached here")
