import cv2
video = cv2.VideoCapture("/Users/sandeepreddy/Documents/fire project/firevideo.MOV")

while(1):
    ret, frame = video.read()
    cv2.imshow('video',frame)
    k = cv2.waitKey(1)
    if k==27:
        break
    
video.release()
cv2.destroyAllWindows()