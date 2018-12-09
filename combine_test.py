from combine import closest_pixel

def test_closest_pixel_1():
    pixel1 = [255,155, 9]
    pixel2 = [155, 255, 10]
    pixel3 = [0,155, 8]
    pixel4 = [89, 208, 190]
    window = [[pixel1, pixel2], [pixel3, pixel4]]

    pixel = [255, 150, 8]

    return closest_pixel(window, pixel) == (0,0)

def test_closest_pixel_2():
    pixel1 = [255,0, 0]
    pixel2 = [0, 255, 0]
    pixel3 = [0,0, 255]
    pixel4 = [255, 0, 255]
    window = [[pixel1, pixel2], [pixel3, pixel4]]

    pixel = [5, 250, 5]
    return closest_pixel(window, pixel) == (0,1)

def test_closest_pixel_3():
    pixel1 = [255,0, 0]
    pixel2 = [0, 255, 0]
    pixel3 = [0,0, 255]
    pixel4 = [255, 0, 255]
    window = [[pixel1, pixel2], [pixel3, pixel4]]

    pixel = [5, 5, 255]
    return closest_pixel(window, pixel) == (1,0)

def test_closest_pixel_4():
    pixel1 = [255,155, 9]
    pixel2 = [155, 255, 10]
    pixel3 = [0,155, 8]
    pixel4 = [89, 208, 190]
    window = [[pixel1, pixel2], [pixel3, pixel4]]

    pixel = [70, 200, 180]

    return closest_pixel(window, pixel) == (1,1)


print test_closest_pixel_1()
print test_closest_pixel_2()
print test_closest_pixel_3()
print test_closest_pixel_4()
