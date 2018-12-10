import cv2
import time
from res_change import res_change
from color_to_bw import color_to_bw
from color_image import color_image
from colorize import colorize
from combine import get_high_res_colored

import scipy
from scipy.misc import imread

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

PATH = 'images/'
HIGH_RES_IMAGE = 'colorized_test.png'

if __name__ == "__main__":

    # Begin with a high resolution colorized image (HiResColor)
    # original_image = cv2.imread(PATH+HIGH_RES_IMAGE)
    # # cv2.imshow('Original', original_image)
    # cv2.imwrite(PATH+'HiResColor_'+HIGH_RES_IMAGE, original_image)

    # # Convert the colorized image to black and white (HiResColor -> HiResBW)
    # high_res_bw_image = color_to_bw(original_image)
    # # cv2.imshow('HiResBW', high_res_bw_image)
    # cv2.imwrite(PATH+'HiResBW_'+HIGH_RES_IMAGE, high_res_bw_image)

    # # Reduce the black and white image to a smaller size (HiResBW -> LoResBW)
    # low_res_bw_image = res_change(high_res_bw_image, .5)
    # cv2.imshow(PATH+'LoResBW', low_res_bw_image)
    # cv2.imwrite(PATH+'LoResBW_'+HIGH_RES_IMAGE, low_res_bw_image)

    # # User marks the smaller black and white image (LoResBW -> LoResMark)
    # low_res_mark_image = cv2.imread(PATH+'LoResMark_colorized_test.png')
    # # low_res_mark_image = color_image('LoResBW_'+HIGH_RES_IMAGE, HIGH_RES_IMAGE)
    # cv2.imshow('LoResMark', low_res_mark_image)

    t1_start = time.perf_counter()
    t2_start = time.process_time()

    # Pass both the LoResBW and LoResMark into the colorizer (LoResBW + LoResMark -> LoResColor)
    pic_o_rgb = imread(PATH+'LoResBW_'+HIGH_RES_IMAGE)
    # low_res_color_image = colorize(low_res_bw_image, low_res_mark_image)
    pic_o = pic_o_rgb.astype(float)/255
    pic_m_rgb = imread(PATH+'LoResMark_colorized_test.png')
    pic_m = pic_m_rgb.astype(float)/255
    low_res_color_image = colorize(pic_o,pic_m)
    # cv2.imshow(PATH+'LoResColor', low_res_color_image)
    # cv2.imwrite(PATH+'LoResColor_'+HIGH_RES_IMAGE, low_res_color_image)

    # Pass the HiResBW, LoResBW, and LoResColor to get smaller marked window (HiResBW + LoResBW + LoResColor -> MarkedWindow)

    # Pass the marked window back into colorizer and recombine to high resolution colorized image (MarkedWindow -> HiResColorRecostructed)
    # high_res_color_reconstructed = get_high_res_colored(

    t1_stop = time.perf_counter()
    t2_stop = time.process_time()
    print("Elapsed time: %.1f [sec]" % ((t1_stop-t1_start)))
    print("CPU process time: %.1f [sec]" % ((t2_stop-t2_start)))

    fig = plt.figure()
    fig.add_subplot(1,2,1).set_title('Black & White')
    imgplot = plt.imshow(pic_o_rgb)
    fig.add_subplot(1,2,2).set_title('Colorized')
    imgplot = plt.imshow(low_res_color_image)
    plt.show();

    cv2.waitKey(0)
    cv2.destroyAllWindows()
