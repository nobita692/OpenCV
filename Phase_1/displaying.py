import cv2
image = cv2.imread("Phase_1/OpenCV Basics.png")

if image is not None :
    cv2.imshow("Image Showing",image)#show the image
    cv2.waitKey(0)#wait for a key
    cv2.destroyAllWindows()#close the window
    
else:
    print("Image not found")
    