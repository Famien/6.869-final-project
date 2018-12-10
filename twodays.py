import cv2
from res_change import res_change
from color_to_bw import color_to_bw
from color_image import color_image
from combine import get_high_res_colored

PATH = 'images/'
HIGH_RES_IMAGE = 'the_dunk.jpeg'

if __name__ == "__main__":
    # Begin with a high resolution colorized image (HiResColor)
    original_image = cv2.imread(PATH+HIGH_RES_IMAGE)
    # cv2.imshow('Original', original_image)
    cv2.imwrite(PATH+'HiResColor_'+HIGH_RES_IMAGE, original_image)

    # Convert the colorized image to black and white (HiResColor -> HiResBW)
    high_res_bw_image = color_to_bw(original_image)
    
    # cv2.imshow('HiResBW', high_res_bw_image)
    cv2.imwrite(PATH+'HiResBW_'+HIGH_RES_IMAGE, high_res_bw_image)

    # Reduce the black and white image to a smaller size (HiResBW -> LoResBW)
    low_res_bw_image = res_change(high_res_bw_image, .5)
    print("twodays : ", PATH, " lowresbwimage: ", low_res_bw_image)
    cv2.imshow(PATH+'LoResBW', low_res_bw_image)
    cv2.imwrite(PATH+'LoResBW_'+HIGH_RES_IMAGE, low_res_bw_image)

    # User marks the smaller black and white image (LoResBW -> LoResMark)
    low_res_mark_image = color_image(PATH+'LoResBW_'+HIGH_RES_IMAGE, HIGH_RES_IMAGE)
    # cv2.imshow('LoResMark', low_res_mark_image)

    
    # Pass both the LoResBW and LoResMark into the colorizer (LoResBW + LoResMark -> LoResColor)

    # Pass the HiResBW, LoResBW, and LoResColor to get smaller marked window and recombine to high resolution colorized image (HiResBW + LoResBW + LoResColor -> HiResColorRecostructed)

#    pic_bw = pic_bw[:,:,:3]
    pic_bw = high_res_bw_image
    high_res_colored = get_high_res_colored(low_res_bw_image, low_res_mark_image, pic_bw, 2)

    cv2.imshow('HiResColored', high_res_colored)
    cv2.imwrite('HiResColored_'+HIGH_RES_IMAGE, high_res_colored)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
