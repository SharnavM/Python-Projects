import cv2
import dropbox
import time
from datetime import datetime
def snap():
    vid_cap =  cv2.VideoCapture(0, cv2.CAP_DSHOW)
    #flag = True
    boolean, frame = vid_cap.read()
    return frame
    #flag = False

    vid_cap.release()
    print("Frame Captured")

def upload(access_token,f,dt):
    name = f
    dbx = dropbox.Dropbox(access_token)
    f = open(f, "rb")
    dbx.files_upload(f.read(), f"/Security/{dt}/{name}")

while True:
    now = datetime.now()
    f = snap()
    dt = now.date()
    ti = now.strftime("%H-%M-%S")
    cv2.imwrite(f"frame_{dt}-{ti}.jpg",f)
    upload("1WY4KQtQnM4AAAAAAAAAAWJ0qRraCzP5CXWJoqzLcudTnxnIALMPGcqsJriEmoX-",f"frame_{dt}-{ti}.jpg", dt)
    time.sleep(10)
