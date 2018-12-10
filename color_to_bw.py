import cv2
import numpy as np

PATH = 'images/'

def color_to_bw(img):
    try:
        bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        bw_three_ch = bw[:,:,None]*np.ones(3, dtype=np.int8)[None,None,:]
        return bw_three_ch
    except Exception as e:
        print(e)
        return str(e)

if __name__ == "__main__":
    img = cv2.imread(PATH+'the_dunk.jpeg')
    bw = color_to_bw(img)
    cv2.imshow('Gray image', bw)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()