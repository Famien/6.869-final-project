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
import numpy as np
import scipy
import scipy.misc


import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

import imageio
from imageio import imread, imwrite

PATH = 'images/'
HIGH_RES_IMAGE = 'colorized_test.png'

if __name__ == "__main__":

    fig = plt.figure()
    # Begin with a high resolution colorized image (HiResColor)
    original_image = imread(PATH+HIGH_RES_IMAGE)
    # cv2.imshow('Original', original_image)
    imwrite(PATH+'HiResColor_'+HIGH_RES_IMAGE, original_image)
    fig.add_subplot(2,2,1).set_title('original')
    imgplot = plt.imshow(original_image)

    # Convert the colorized image to black and white (HiResColor -> HiResBW)
    high_res_bw_image = color_to_bw(original_image)
    # cv2.imshow('HiResBW', high_res_bw_image)
    fig.add_subplot(2,2,2).set_title('black and white')
    imgplot = plt.imshow(high_res_bw_image)
    imwrite(PATH+'HiResBW_'+HIGH_RES_IMAGE, high_res_bw_image)

    # # Reduce the black and white image to a smaller size (HiResBW -> LoResBW)
    low_res_bw_image = res_change(high_res_bw_image, .5)
    # cv2.imshow(PATH+'LoResBW', low_res_bw_image)
    fig.add_subplot(2,2,3).set_title('low_res bw')
    imgplot = plt.imshow(low_res_bw_image)
    imwrite(PATH+'LoResBW_'+HIGH_RES_IMAGE, low_res_bw_image)

    # User marks the smaller black and white image (LoResBW -> LoResMark)
    low_res_mark_image = cv2.imread(PATH+'LoResMark_'+HIGH_RES_IMAGE)
    # low_res_mark_image = color_image('LoResBW_'+HIGH_RES_IMAGE, HIGH_RES_IMAGE)
    fig.add_subplot(2,2,4).set_title('marked low_res bw')
    imgplot = plt.imshow(imread(PATH+'LoResMark_'+HIGH_RES_IMAGE))
    plt.show();

    # cv2.imshow('LoResMark', low_res_mark_image)

    # read in images

    # # pic_o_rgb = low_res_bw_image[:,:,None]*np.ones(3, dtype=np.int8)[None,None,:]
    pic_o_rgb = scipy.misc.imread(PATH+'LoResBW_colorized_test.png')
    pic_o = pic_o_rgb.astype(float)/255
    # # pic_m_rgb = low_res_mark_image[:,:,None]*np.ones(3, dtype=np.int8)[None,None,:]
    pic_m_rgb = scipy.misc.imread(PATH+'LoResMark_colorized_test.png')
    pic_m = pic_m_rgb.astype(float)/255


    ## Colorize on using expanded colorize of low res
    t1_start = time.perf_counter()
    t2_start = time.process_time()
    
    # get colorized versino of low res
    low_res_color_image = colorize(pic_o,pic_m)
    high_res_bw_image = high_res_bw_image.astype(float)/255
    # cv2.imshow('LoResColor', low_res_color_image)
    # get colorized version of high res

    high_res_color_reconstructed = get_high_res_colored4(pic_o, low_res_color_image, high_res_bw_image,2)
    imwrite(PATH+'HiResColorReconstructed_'+HIGH_RES_IMAGE, high_res_color_reconstructed)
    high_res_color_image = colorize(high_res_bw_image,high_res_color_reconstructed)
    imwrite(PATH+'HiResColorRecolored_'+HIGH_RES_IMAGE, high_res_color_image)
    t1_stop = time.perf_counter()
    t2_stop = time.process_time()
    print("Elapsed time: %.1f [sec]" % ((t1_stop-t1_start)))
    print("CPU process time: %.1f [sec]" % ((t2_stop-t2_start)))

    fig = plt.figure()
    fig.add_subplot(1,2,1).set_title('Reconstructed')
    imgplot = plt.imshow(high_res_bw_image)
    fig.add_subplot(1,2,2).set_title('Colorized')
    imgplot = plt.imshow(high_res_color_image)
    plt.show();

    cv2.waitKey(0)
    cv2.destroyAllWindows()
