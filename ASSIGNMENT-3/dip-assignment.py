import cv2 as cv

img = cv.imread('img.jpeg')
cv.imshow('Original Image', img)

gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image', gray_image)

adaptive_thresh_image = cv.adaptiveThreshold(
    gray_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow('Adaptive Threshold Image', adaptive_thresh_image)

blurred_image = cv.GaussianBlur(gray_image, (5, 5), 0)
cv.imshow('Blurred Image', blurred_image)

_, otsu_thresh_image = cv.threshold(
    blurred_image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
cv.imshow('Otsu Threshold Image', otsu_thresh_image)

cv.waitKey(0)
cv.destroyAllWindows()
