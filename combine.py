def distance(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2])

def closest_pixel(window, pixel):
    smallest_distance = 999 # largest intensity value is smaller than this
    closest_pixel = None

    for i in range(len(window)):
        for j in range(len(window[0])):
            window_pixel = window[i][j]
            distance = distance(pixel,window_pixel)
            if distance < smallest_distance:
                closest_pixel = (i,j)
                smallest_distance = distance
                
    return closest_pixel


def color_window(c_image, c_window, i, j):
    c_image[i][j] = c_window[0][0]
    c_image[i+1][j] = c_window[1][0]
    c_image[i][j+1] = c_window[0][1]
    c_image[i+1][j+1] = c_window[1][1]
    

def get_highres_colored(lr_bw, lr_colored, hr_bw):
    """ Returns a colorized version of a a b/w image using a low-res colorized version
    
    Args: lr_colored: low-res colored image
          hr_bw:      high-res bw image

    Returns:
        Image: colorized version of the b/w image
    
    """
    colorized_image = hr_bw[:]
    for i in range(len(hr_bw))/2:
        for j in range(len(hr_bw[0]))/2:
            window = hr_bw[i:i+2][j:j+2]
            lr_pixel = lr_bw[i/2][j/2] # find corresponding pixel in low res version
            closest = closest_pixel(window, lr_pixel)
            # color pixel closest in intensity to low res to that pixel's color in colorized low res
            window_marked = window[:]
            window_marked[closest[0]][closest[1]] = lr_colored[i/2][j/2]
            colorized_window = colorize(window, window_marked)
            color_window(colorized_image, colorized_window,i ,j)


import cv2
from res_change import res_change
from color_to_bw import color_to_bw



