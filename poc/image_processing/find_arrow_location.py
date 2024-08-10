import cv2


                        #   y    x
current_cam_board_begin = [223, 166]
current_cam_board_end = [797, 1125]
used_height_average = 80


def pixel_is_white(pixel):
    return pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255


def find_arrow_location(image):
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
        return (height, average_x)
    else:
        print("No white pixel found")
        return (0, 0)


image = cv2.imread("./data/example_results/image_difference/mask_0.jpg")

y, x = find_arrow_location(image)

for i in range(y -5, y+5):
    for j in range(x-5, x+5):
        image[i, j] = (255, 0, 0)

cv2.imwrite("./data/example_results/arrow_position/arrow_0.jpg", image)