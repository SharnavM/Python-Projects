import cv2
import dropbox
import os
def snap():
    vid_cap = cv2.VideoCapture(0)
    flag = True
    os.chdir("A:\WhiteHatJr\Python\C102")
    while flag:
       boolean, frame = vid_cap.read()
       print("frane ", frame)
       print(boolean)
       cv2.imwrite("./frame.jpg",frame)
       flag = False

    vid_cap.release()
    cv2.destroyAllWindows()
    print("Frame Captured")

snap()
