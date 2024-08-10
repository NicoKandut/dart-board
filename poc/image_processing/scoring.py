from PIL import Image
import numpy as np
import cv2;

# distances
DOUBLE_BULL = 12.7 / 2
BULL = 31.8 / 2
DOUBLE_INNER = 107 - 8
DOUBLE_OUTER = 107
TRIPLE_INNER = 170 - 8
TRIPLE_OUTER = 170

order = [6,13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10]

origin = np.array([0,0])

def score_xy(xy) -> float:
    distance = np.linalg.norm(xy - origin)
    angle = np.arctan2(xy[1], xy[0]) * 180 / np.pi
    return score_da(distance, angle)

def score_da(distance: float, angle: float) -> float:

    # distance based scoring
    if(distance < DOUBLE_BULL):
        return 50
    if(distance < BULL):
        return 25
    if(distance > TRIPLE_OUTER):
        return 0
    
    # angle based scoring
    points = order[int(((angle + 9) % 360) / 18)]

    if(distance < DOUBLE_INNER):
        return points
    if(distance < DOUBLE_OUTER):
        return points * 3
    if(distance < TRIPLE_INNER):
        return points
    if(distance < TRIPLE_OUTER):
        return points * 2
    
    return 0
    

triple_20 = score_da(0.55, 90.0) # 50

print(triple_20)    
    

output_resolution = 500
half_resolution = output_resolution / 2

output = np.zeros((output_resolution,output_resolution,3), np.uint8)

for y in range(output_resolution):
    y_scaled = (y - half_resolution) / half_resolution * -180
    for x in range(output_resolution):
        x_scaled = (x - half_resolution) / half_resolution * 180

        # print(x_scaled, y_scaled)

        score = score_xy(np.array([x_scaled, y_scaled]))
        output[y,x] = (score * 4, score * 4, score * 4)

cv2.imwrite("out_score.jpg", output)


    
