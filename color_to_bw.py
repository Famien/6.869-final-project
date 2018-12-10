import cv2

PATH = 'images/'

def color_to_bw(img):
    try:
        image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return image
    except Exception as e:
        print(e)
        return str(e)

if __name__ == "__main__":
    img = cv2.imread(PATH+'the_dunk.jpeg')
    bw = color_to_bw(img)
    cv2.imshow('Gray image', bw)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()