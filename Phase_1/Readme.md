cv2.imread()	Image Read - Loads an image from a specified file path and returns it as a multi-dimensional array (cv2.Mat in C++, NumPy array in Python).

cv2.imwrite()	Image Write - Saves an image (a NumPy array or cv2.Mat) to the specified file path. The file extension (e.g., .jpg, .png) determines the saving format.

cv2.imshow()	Image Show - Displays an image in a designated window.

cv2.waitKey()	A keyboard binding function that waits for a specified time (in milliseconds) or until a key is pressed. It's necessary to keep the window open after cv2.imshow(). A value of 0 means it waits indefinitely.

cv2.destroyAllWindows()	Destroys all the OpenCV windows that were created.

.shape	(As a NumPy array attribute) Returns a tuple representing the dimensions of the image: (height, width, channels). For grayscale images, it returns (height, width).

cv2.resize()	Resizes an image to a specified size. Essential for aligning images or adapting them to different processing requirements.

cv2.cvtColor()	Converts an image from one color space to another, such as BGR (Blue-Green-Red), which is OpenCV's default format, to Grayscale or HSV (Hue-Saturation-Value).

cv2.split()	Splits a multi-channel image (like BGR) into individual single-channel images (e.g., separate Blue, Green, and Red arrays).

cv2.merge()	Merges multiple single-channel arrays back into a multi-channel image.