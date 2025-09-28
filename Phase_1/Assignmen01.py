# 1. Load a image
# 2.convert in Grayscale
# 3. Show
# 4. Save
#Challanges ->  take image location as an input
 #               ask to user that they just want to "show" image or "save"
 #               If user choose "save" ,take ouptut image name also from the user    
 #               Dislpay massage "File Name Saved Successfuly"            




import cv2
import sys
image_loc = input("Put Image Location :")
image = cv2.imread(image_loc)
if image is None:
    print(f"Could Not load Image from {image_loc}")
    sys.exit()

gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

option = input("1.Save\n2.show\nChoose Option :")

if (option=="1"):
    cv2.imwrite("new_pic.png",gray)
    print("File Name Saved Successfuly")
    
elif(option=="2"):
    cv2.imshow("This is your Image:",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Could not load Image")
