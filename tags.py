import cv2
import apriltag as ap

vid = cv2.VideoCapture(0)

aprilcount = 0

def detect_apriltags():
    temp = 0
    # read frame
    ret, frame = vid.read()
    # show camera
    cv2.imshow('Vision', frame)
    # check for 36h11 apriltags
    options = ap.DetectorOptions(families="tag36h11")
    results = ap.Detector(options).detect(cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))
    if results:
        # if an apriltag was detected, increase count
        temp+=1
    return temp

while(True):
    aprilcount += detect_apriltags()
    # exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
print("{} total AprilTags detected".format(aprilcount))