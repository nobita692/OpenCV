import cv2
image = cv2.imread("Phase_1/OpenCV Basics.png")

if image is not None:
    success = cv2.imwrite("output_OpenCv.png",image)
    if success:
        print("Image save successfull as as 'output_OpenCv'")
    else:
        print("Failed to save an Image")
        
else:
    print("Error: Could not load image")
    
        