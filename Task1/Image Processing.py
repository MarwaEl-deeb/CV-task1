import cv2
image = cv2.imread("C:/Users/marwa/OneDrive/Desktop/CV task1/images/codes.png")
print(image)
# resizing image
Resized_Image = cv2.resize(image, (850, 550))
cv2.imshow("Image Frame", Resized_Image)
cv2.waitKey(0)
# stroring the resized image
cv2.imwrite("Resized Image.png", Resized_Image)