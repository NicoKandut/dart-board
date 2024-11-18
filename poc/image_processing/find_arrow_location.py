import cv2
import numpy
                        #   y    x
current_cam_board_begin = [223, 166]
current_cam_board_end = [797, 1125]
used_height_average = 20


def pixel_is_white(pixel):
    return pixel[0] > 240 and pixel[1] > 240 and pixel[2] > 240

def add_point(image, x, y):
    for i in range(y -5, y+5):
        for j in range(x-5, x+5):
            image[i, j] = (255, 0, 0)

    return image

def find_arrow_location(image):
    kernel = numpy.ones((2, 4), numpy.uint8)

    image = cv2.erode(image, kernel)
    image = cv2.erode(image, kernel)
    image = cv2.dilate(image, kernel)
    image = cv2.dilate(image, kernel)

    height = 0

    y = current_cam_board_end[0]
    while y > current_cam_board_begin[0] and height == 0:

        x = current_cam_board_end[1]
        while x > current_cam_board_begin[1] and height == 0:
            pixel = image[y, x]

            if pixel_is_white(pixel):
                height = y
            x = x -1
        y = y -1

    x_coords = []
    if height != 0:
        y = height
        while y > height - used_height_average:
            x = current_cam_board_end[1]
            while x > current_cam_board_begin[1]:
                pixel = image[y, x]
                if pixel_is_white(pixel):
                    x_coords.append(x)

                x = x -1
            y = y -1
    
        average_x = int(sum(x_coords) / len(x_coords))

        # show dart board box
        # image = cv2.rectangle(image, (current_cam_board_begin[1], current_cam_board_begin[0]), (current_cam_board_end[1], current_cam_board_end[0]), (0,255,0))
        
        # show transformed image
        # cv2.imshow("result", add_point(image, average_x, height))
        # cv2.waitKey(0)
        return (height, average_x)
    else:
        print("No white pixel found")
        return (0, 0)


image = cv2.imread("./data/example_results/image_difference/mask_0.jpg")

y, x = find_arrow_location(image)

image = add_point(image, x, y)

cv2.imwrite("./data/example_results/arrow_position/arrow_0.jpg", image)