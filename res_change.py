import cv2

def res_change(img, scale):
    try:
        image = cv2.imread(img)
        width, height, _ = image.shape
        image = cv2.resize(image, (0,0), fx=scale, fy=scale)
        return image
    except Exception as e:
        print("Error")
        print(e)
        return str(e)

if __name__ == "__main__":
    image = 'the_dunk.jpeg'
    cv2.imshow("original image", cv2.imread(image))
    resize = res_change(image, .5)
    cv2.imshow('Resized image', resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
