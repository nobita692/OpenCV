cv2.imread()	Image Read - Loads an image from a specified file path and returns it as a multi-dimensional array (cv2.Mat in C++, NumPy array in Python).

cv2.imwrite()	Image Write - Saves an image (a NumPy array or cv2.Mat) to the specified file path. The file extension (e.g., .jpg, .png) determines the saving format.

cv2.imshow()	Image Show - Displays an image in a designated window.

cv2.waitKey()	A keyboard binding function that waits for a specified time (in milliseconds) or until a key is pressed. It's necessary to keep the window open after cv2.imshow(). A value of 0 means it waits indefinitely.

cv2.destroyAllWindows()	Destroys all the OpenCV windows that were created.

