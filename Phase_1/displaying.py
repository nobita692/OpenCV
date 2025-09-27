import cv2
image = cv2.imread("Phase_1/OpenCV Basics.png")

if image is not None :
    cv2.imshow("Image Showing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Image not found")
    