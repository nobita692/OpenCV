# 4. Dimetion
import cv2
image = cv2.imread("Phase_1/OpenCV Basics.png")

if image is not None :
    h,w,c = image.shape
    print(f"Image Loaded->\nHeight: {h}\nWidth: {w}\nColor_Channels: {c}")
else:
    print("Could Not load Image")