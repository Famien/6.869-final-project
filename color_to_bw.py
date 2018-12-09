import cv2

img = 'the_dunk.jpeg'
image = cv2.imread(img)
cv2.imshow('original image', image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()