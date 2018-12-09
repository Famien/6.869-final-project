import cv2

def color_to_bw(img):
    try:
        image = cv2.imread(img)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray
    except Exception as e:
        print('Error')
        return str(e)

if __name__ == "__main__":
    img = 'the_dunk.jpeg'
    bw = color_to_bw(img)
    cv2.imshow('Gray image', bw)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()