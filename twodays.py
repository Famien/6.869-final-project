import cv2
from res_change import res_change
from color_to_bw import color_to_bw

HIGH_RES_IMAGE = 'the_dunk.jpeg'

if __name__ == "__main__":
    # Begin with a high resolution colorized image (HiResColor)
    original_image = cv2.imread(HIGH_RES_IMAGE)
    cv2.imshow('Original', original_image)
    cv2.imwrite('HiResColor_'+HIGH_RES_IMAGE, original_image)

    # Convert the colorized image to black and white (HiResColor -> HiResBW)
    high_res_bw_image = color_to_bw(original_image)
    cv2.imshow('HiResBW', high_res_bw_image)
    cv2.imwrite('HiResBW_'+HIGH_RES_IMAGE, high_res_bw_image)

    # Reduce the black and white image to a smaller size (HiResBW -> LoResBW)
    low_res_bw_image = res_change(high_res_bw_image, .5)
    cv2.imshow('LoResBW', low_res_bw_image)
    cv2.imwrite('LoResBW_'+HIGH_RES_IMAGE, low_res_bw_image)

    # User marks the smaller black and white image (LoResBW -> LoResMark)

    # Pass both the LoResBW and LoResMark into the colorizer (LoResBW + LoResMark -> LoResColor)

    # Pass the HiResBW, LoResBW, and LoResColor to get smaller marked window (HiResBW + LoResBW + LoResColor -> MarkedWindow)

    # Pass the marked window back into colorizer and recombine to high resolution colorized image (MarkedWindow -> HiResColorRecostructed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()