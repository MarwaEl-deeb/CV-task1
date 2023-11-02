import cv2

# to take frames from the camera
video = cv2.VideoCapture(0)

# to take frame from an existing video
#video = cv2.VideoCapture("C:/Users/marwa/OneDrive/Desktop/CV task1/images/Time Complixity.mp4")

while True:
    status, frame = video.read()
    print(frame)
# resizing the video
    resized_frames = cv2.resize(frame, (1000, 700))
    cv2.imshow("VideoCapture",  resized_frames)
    if cv2.waitKey(20) & 0xff == ord("Q"):
        break
video.release()
cv2.destroyAllWindows()
