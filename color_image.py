import cv2
import numpy as np

PATH = 'images/'
drawing = False # true if mouse is pressed

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(image,(x,y),RADIUS,COLOR,-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(image,(x,y),RADIUS,COLOR,-1)

def color_image(img, name):
    global image, COLOR, RED, GREEN, BLUE, CYAN, YELLOW, RADIUS
    RED = (0,0,255)
    GREEN = (0,255,0)
    BLUE = (255,0,0)
    CYAN = (255,255,0)
    YELLOW = (0,255,255)
    COLOR = RED
    RADIUS = 5
    print("Path: ", PATH, " img: ", img)
    image = cv2.imread(img)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)

    while(1):
        cv2.imshow('image',image)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('s'):
            cv2.imwrite(PATH+'LoResMark_'+name,image)
            break
        elif k == ord('g'):
            COLOR = GREEN
        elif k == ord('b'):
            COLOR = BLUE
        elif k == ord('r'):
            COLOR = RED
        elif k == ord('y'):
            COLOR = YELLOW
        elif k == ord('c'):
            COLOR = CYAN
        elif k == ord('n'):
            RADIUS = max(RADIUS-1, 1)
        elif k == ord('m'):
            RADIUS = min(RADIUS+1,100)
        elif k == 27:
            cv2.imwrite(PATH+'LoResMark_'+name,image)
            break

    cv2.destroyAllWindows()
    return image

if __name__ == "__main__":
    color_image('maplestory.jpg','maplestory.jpg')
