import cv2
image = cv2.imread("Phase_1/Tony.jpg")#read the image

if image is None:
    print("Error: Image path is empty")
    
else:
    print("Image loaded Successfully")