def closest_pixel(window, pixel):
    smallest_distance = 999 # largest intensity value is smaller than this
    closest_pixel = None
    
    pixel = window[0][0]
    distance = abs(pixel[0] - pixel[0])
    if distance < smallest_distance:
        closest_pixel = (0,0)

    return closest_pixel


for i in image.cols/2:
    for j in image.rows/2:
        window = image[i:i+2, j:j+2]
        lr_pixel = low_res[i/2][j/2]
        closest = window_pixel_closest()
    window_copy = window[:]
    color_pixel(window_copy, lr_pixel)
    new_window = colorize(window, window_copy)


