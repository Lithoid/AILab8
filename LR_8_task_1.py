import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("holovetskiy.png")
# DISPLAY
cv2.imshow("holovetskiy", img)
cv2.waitKey(0)