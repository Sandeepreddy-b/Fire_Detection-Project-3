import cv2
photo = cv2.imread("IMG_6621.jpeg") #photo name

cv2.imshow("Image",photo) # to display the photo with given title in double quotes
cv2.waitKey(0)
cv2.destroyAllWindows

#destro all windows is to close the tabs that were open after pressing escape key