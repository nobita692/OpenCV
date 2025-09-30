import cv2
image = cv2.imread(" OpenCV/Phase_2/Phase2content.png")

if image is None:
    print("Image Not Found")

else:
    print("Image Loaded")
    
    resized = cv2.resize(image, (250, 250))
    
    cv2.imshow("Original Image :", image)
    cv2.imshow("Resized Image:", resized)
    
    cv2.imwrite("Edited_Output.png", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    