from colorize import colorize
from imageio import imread, imwrite
import cv2
import matplotlib.pyplot as plt

PATH = 'images/'
def get_distance(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2])

def closest_pixel(window, pixel):
    smallest_distance = 999 # largest intensity value is smaller than this
    closest_pixel = None
    for i in range(len(window)):
        for j in range(len(window)):
            window_pixel = window[i,j]
            distance = get_distance(pixel,window_pixel)
            if distance < smallest_distance:
                closest_pixel = (i,j)
                smallest_distance = distance
                
    return closest_pixel

def color_window(image_to_color, colored_window, i_index, j_index):
    for i in range(len(colored_window)):
        for j in range(len(colored_window[0])):
            image_to_color[i_index+i,j_index+j] = colored_window[i][j]

def get_high_res_colored(lr_bw, lr_colored, hr_bw, window_size):
    """ Returns a colorized version of a a b/w image using a low-res colorized version
    
    Args: lr_colored: low-res colored image
          hr_bw:      high-res bw image

    Returns:
        Image: colorized version of the b/w image
    
    """
    colorized_image = hr_bw[:]

    for i in range(int(len(hr_bw)/window_size)):
        i_start = i*window_size
        i_end = i*window_size + 2
        for j in range(int(len(hr_bw)/window_size)):
            j_start = j*window_size
            j_end = j*window_size + 2

            window = hr_bw[i_start:i_end,j_start:j_end]

            lr_pixel = lr_bw[i,j] # find corresponding pixel in low res version
            closest = closest_pixel(window, lr_pixel)
            # color pixel closest in intensity to low res to that pixel's color in colorized low res
            window_marked = window[:]
            # for k in range(window_size):
#                 for l in range(window_size):
#                     window_marked[k, l] = lr_colored[i,j]
#colorized_window = window_marked

            window_marked[closest[0],closest[1]] = lr_colored[i,j]
            colorized_window = colorize(window, window_marked)

            color_window(colorized_image, colorized_window,i*window_size ,j*window_size)

    return colorized_image

def get_high_res_colored2(lr_bw, lr_colored, hr_bw, window_size):
    """ Returns a colorized version of a a b/w image using a low-res colorized version
    
    Args: lr_colored: low-res colored image
          hr_bw:      high-res bw image

    Returns:
        Image: colorized version of the b/w image
    
    """
    colorized_image = hr_bw[:]

    for i in range(int(len(hr_bw)/window_size)):
        i_start = i*window_size
        i_end = i*window_size + 2
        for j in range(int(len(hr_bw)/window_size)):
            j_start = j*window_size
            j_end = j*window_size + 2

            window = hr_bw[i_start:i_end,j_start:j_end]

            lr_pixel = lr_bw[i,j] # find corresponding pixel in low res version
            closest = closest_pixel(window, lr_pixel)
            # color pixel closest in intensity to low res to that pixel's color in colorized low res
            window_marked = window[:]
            window_marked[closest[0],closest[1]] = lr_colored[i,j]

            color_window(colorized_image, window_marked, i*window_size ,j*window_size)

    return colorized_image

def get_high_res_colored3(lr_bw, lr_colored, hr_bw, window_size):
    """ Returns a colorized version of a a b/w image using a low-res colorized version
    
    Args: lr_colored: low-res colored image
          hr_bw:      high-res bw image

    Returns:
        Image: colorized version of the b/w image
    
    """
    colorized_image = hr_bw[:]

    for i in range(int(len(hr_bw)/window_size)):
        i_start = i*window_size
        i_end = i*window_size + 2
        for j in range(int(len(hr_bw)/window_size)):
            j_start = j*window_size
            j_end = j*window_size + 2

            window = hr_bw[i_start:i_end,j_start:j_end]

            lr_pixel = lr_bw[i,j] # find corresponding pixel in low res version
            closest = closest_pixel(window, lr_pixel)
            # color pixel closest in intensity to low res to that pixel's color in colorized low res
            window_marked = window[:]
            for k in range(window_size):
                for l in range(window_size):
                    window_marked[k, l] = lr_colored[i,j]
            colorized_window = window_marked

#            window_marked[closest[0],closest[1]] = lr_colored[int(i/window_size),int(j/window_size)]
#            colorized_window = colorize(window, window_marked)

            color_window(colorized_image, colorized_window,i*window_size ,j*window_size)

    return colorized_image

def get_high_res_colored4(lr_bw, lr_colored, hr_bw, window_size):
    """ Returns a colorized version of a a b/w image using a low-res colorized version
    
    Args: lr_colored: low-res colored image
          hr_bw:      high-res bw image

    Returns:
        Image: colorized version of the b/w image
    
    """
    colorized_image = hr_bw[:]

    for i in range(int(len(hr_bw)/window_size)):
        i_start = i*window_size
        i_end = i*window_size + 2
        for j in range(int(len(hr_bw)/window_size)):
            j_start = j*window_size
            j_end = j*window_size + 2

            window = hr_bw[i_start:i_end,j_start:j_end]

            lr_pixel = lr_bw[i,j] # find corresponding pixel in low res version
            closest = closest_pixel(window, lr_pixel)
            # color pixel closest in intensity to low res to that pixel's color in colorized low res
            window_marked = window[:]
            window_marked[closest[0],closest[1]] = lr_colored[i,j]

            color_window(colorized_image, window_marked, i*window_size ,j*window_size)

    return colorized_image
