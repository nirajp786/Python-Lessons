from cv2 import cv2

img = cv2.imread("galaxy.jpg", 0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_img = cv2.resize(img,(img.shape[1]//2, img.shape[0]//2))
cv2.imshow("Galaxy", resized_img)
cv2.imwrite("Galaxy Resized.jpg", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()