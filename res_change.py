import cv2

PATH = 'images/'

def res_change(img, scale):
    try:
        width, height = img.shape[0:2]
        image = cv2.resize(img, (0,0), fx=scale, fy=scale)
        return image
    except Exception as e:
        print(e)
        return str(e)

if __name__ == "__main__":
    img = cv2.imread(PATH+'the_dunk.jpeg')
    resize = res_change(img, .5)
    cv2.imshow('Resized image', resize)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
