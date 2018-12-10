import cv2
import time
from res_change import res_change
from color_to_bw import color_to_bw
from color_image import color_image
from colorize import colorize
from combine import get_high_res_colored
from combine import get_high_res_colored2
from combine import get_high_res_colored3
from combine import get_high_res_colored4

import scipy
from scipy.misc import imread

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

PATH = 'images/'
HIGH_RES_IMAGE = 'the_dunk.jpeg'

if __name__ == "__main__":

    # Begin with a high resolution colorized image (HiResColor)
    original_image = cv2.imread(PATH+HIGH_RES_IMAGE)
    # # cv2.imshow('Original', original_image)
    cv2.imwrite(PATH+'HiResColor_'+HIGH_RES_IMAGE, original_image)

    # # Convert the colorized image to black and white (HiResColor -> HiResBW)
    high_res_bw_image = color_to_bw(original_image)
    # # cv2.imshow('HiResBW', high_res_bw_image)
    cv2.imwrite(PATH+'HiResBW_'+HIGH_RES_IMAGE, high_res_bw_image)

    # # Reduce the black and white image to a smaller size (HiResBW -> LoResBW)
    low_res_bw_image = res_change(high_res_bw_image, .5)
    # cv2.imshow(PATH+'LoResBW', low_res_bw_image)
    cv2.imwrite(PATH+'LoResBW_'+HIGH_RES_IMAGE, low_res_bw_image)

    # # User marks the smaller black and white image (LoResBW -> LoResMark)
    #low_res_mark_image = cv2.imread(PATH+'LoResMark_colorized_test.png')
    low_res_mark_image = color_image('LoResBW_'+HIGH_RES_IMAGE, HIGH_RES_IMAGE)
    # cv2.imshow('LoResMark', low_res_mark_image)




    # read in images
    pic_o_rgb = imread(PATH+'LoResBW_'+HIGH_RES_IMAGE)
    pic_o = pic_o_rgb.astype(float)/255
    pic_m_rgb = imread(PATH+'LoResMark_colorized_test.png')
    pic_m = pic_m_rgb.astype(float)/255
    pic_high_res_bw_rgb = imread(PATH + 'HiResBW_'+ HIGH_RES_IMAGE)
    pic_high_res_bw = pic_high_res_bw_rgb.astype(float)/255
    pic_high_res_mark_rgb = imread(PATH + 'HiResMark_' + HIGH_RES_IMAGE)
    pic_high_res_mark = pic_high_res_mark_rgb.astype(float)/255

    ### Normal Colorization
    ###
    # time colorization process
    t1_start = time.perf_counter()
    t2_start = time.process_time()
    
    # get colorized versino of low res
    high_res_color_image = colorize(pic_high_res_bw,pic_high_res_mark)

    # get colorized version of high res
    t1_stop = time.perf_counter()
    t2_stop = time.process_time()
    print("Elapsed time: %.1f [sec]" % ((t1_stop-t1_start)))
    print("CPU process time: %.1f [sec]" % ((t2_stop-t2_start)))

    fig = plt.figure()
    fig.add_subplot(1,2,1).set_title('Black & White')
    imgplot = plt.imshow(pic_o_rgb)
    fig.add_subplot(1,2,2).set_title('Colorized')
    imgplot = plt.imshow(high_res_color_image)
    plt.show();

    ### Colorize on using expanded colorize of low res
    t1_start = time.perf_counter()
    t2_start = time.process_time()
    
    # get colorized versino of low res
    low_res_color_image = colorize(pic_o,pic_m)

    # get colorized version of high res
    high_res_color_reconstructed = get_high_res_colored4(pic_o, low_res_color_image, pic_high_res_bw,2)
    high_res_color_image = colorize(pic_high_res_bw,high_res_color_reconstructed)
    t1_stop = time.perf_counter()
    t2_stop = time.process_time()
    print("Elapsed time: %.1f [sec]" % ((t1_stop-t1_start)))
    print("CPU process time: %.1f [sec]" % ((t2_stop-t2_start)))

    fig = plt.figure()
    fig.add_subplot(1,2,1).set_title('Black & White')
    imgplot = plt.imshow(pic_o_rgb)
    fig.add_subplot(1,2,2).set_title('Colorized')
    imgplot = plt.imshow(high_res_color_image)
    plt.show();

    
    # Colorize using windows 2x2
    # time colorization process
#     t1_start = time.perf_counter()
#     t2_start = time.process_time()
    
#     # get colorized versino of low res
#     low_res_color_image = colorize(pic_o,pic_m)

#     # get colorized version of high res
#     high_res_color_reconstructed = get_high_res_colored(pic_o, low_res_color_image, pic_high_res_bw,2)
#     t1_stop = time.perf_counter()
#     t2_stop = time.process_time()
#     print("Elapsed time: %.1f [sec]" % ((t1_stop-t1_start)))
#     print("CPU process time: %.1f [sec]" % ((t2_stop-t2_start)))

#     fig = plt.figure()
#     fig.add_subplot(1,2,1).set_title('Black & White')
#     imgplot = plt.imshow(pic_o_rgb)
#     fig.add_subplot(1,2,2).set_title('Colorized')
#     imgplot = plt.imshow(high_res_color_reconstructed)
#     plt.show();

    cv2.waitKey(0)
    cv2.destroyAllWindows()
