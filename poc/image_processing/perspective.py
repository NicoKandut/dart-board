from PIL import Image
import numpy as np
import cv2;


in_path = "./input_2.jpg"
out_path = "./out_3.jpg"
output_resolution = 1500

# img_origin = np.array([468,2111])
# img_x_hat = np.array([1662,300])
# img_y_hat = np.array([1272,3593])
# img_far = np.array([1770,1986])

img_origin = np.array([846,76])
img_x_hat = np.array([1779,1148])
img_y_hat = np.array([651,3857])
img_far = np.array([1674,2905])

image_corners = np.float32([
    img_origin,
    img_x_hat,
    img_far,
    img_y_hat
])

output_corners = np.float32([
    [0.0,0.0],
    [output_resolution,0.0],
    [output_resolution,output_resolution],
    [0.0,output_resolution]
])

transform = cv2.getPerspectiveTransform(image_corners, output_corners)

print(transform)

src_image = cv2.imread(in_path) 
hh, ww = src_image.shape[:2]
imgOutput = cv2.warpPerspective(src_image, transform, (ww,hh), cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0,0))
cv2.imwrite("out_3_2.jpg", imgOutput[0:output_resolution, 0:output_resolution])

