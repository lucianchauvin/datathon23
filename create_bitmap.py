from read_data import get_data
import numpy as np
<<<<<<< HEAD
import json
=======
import math
>>>>>>> c9b8e0866a227fad323c9cca8d2481df0f656dbb

BITMAP_SIZE = 256
STROKE_RADIUS = 5

<<<<<<< HEAD

def get_data(filename):
    with open(filename, "r") as infile:
        for line in infile:
            line = line.rstrip()

            jsonObj = json.loads(line)

            yield jsonObj

def generate_bitmap(filename):
    ndjson_generator = get_data(filename)
    for json_obj in ndjson_generator:
        # create 2D array
        bitmap = np.zeros((BITMAP_SIZE, BITMAP_SIZE), dtype=np.float_)
=======
def generate_bitmap(filename):
    for json_obj in get_data(filename):
        # create 2D array
        bitmap = np.ones((BITMAP_SIZE, BITMAP_SIZE), dtype=bool)
>>>>>>> c9b8e0866a227fad323c9cca8d2481df0f656dbb

        strokes = json_obj["drawing"]

        # go through the strokes
        for stroke in strokes:
            # get each point in the stroke
            x_vals = stroke[0]
            y_vals = stroke[1]

            for point_num in range(len(x_vals) - 1):
                x1, y1 = x_vals[point_num], y_vals[point_num]
                x2, y2 = x_vals[point_num + 1], y_vals[point_num + 1]

<<<<<<< HEAD
                if x1 == x2:
                    for y in range(y1, y2, 2 * (x1 < x2) - 1):
                        bitmap[y][x1] = 1
                    continue

                m = (y2 - y1) / (x2 - x1)
                b = y1 - m * x1
                prev_y = y1
                for x in range(x1, x2 + 1, 2 * (x1 < x2) - 1):
                    y = round(m*x + b)
                    
                    bitmap[y][x] = 1

                    if abs(prev_y - y) > 1:
                        for inter_y in range(prev_y, y, 2 * (x1 < x2) - 1):
                            bitmap[inter_y][x] = 1
=======
                if x2 < x1:
                    x1, x2, y1, y2 = x2, x1, y2, y1

                start_x = x1 - STROKE_RADIUS
                final_x = x2 + STROKE_RADIUS
                start_y = (y1 if y1 < y2 else y2) - STROKE_RADIUS
                final_y = (y2 if y1 < y2 else y1) + STROKE_RADIUS

                if start_x < 0:
                    start_x = 0
                if final_x >= BITMAP_SIZE:
                    final_x = BITMAP_SIZE - 1
                if start_y < 0:
                    start_y = 0
                if final_y >= BITMAP_SIZE:
                    final_y = BITMAP_SIZE - 1
>>>>>>> c9b8e0866a227fad323c9cca8d2481df0f656dbb

                start_point = np.array([x1, y1])
                end_point = np.array([x2, y2])
                line_vec = end_point - start_point
                for x in range(start_x, final_x):
                    prev_distance = 0
                    distance = 0
                    for y in range(start_y, final_y):
                        point_vec = np.array([x, y]) - start_point
                        prev_distance = distance

                        # find distance
                        projection = (point_vec @ line_vec) * line_vec / (line_vec @ line_vec)
                        point = projection + start_point

                        # check if point within the line segment
                        if point[0] < x1:
                            distance = math.sqrt(point_vec @ point_vec)
                        elif point[0] > x2:
                            distance = math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
                        else:
                            # along the line
                            distance_vec = point_vec - projection
                            distance = math.sqrt(distance_vec @ distance_vec)

                        if distance <= STROKE_RADIUS:
                            bitmap[y][x] = 0
                        elif prev_distance != 0 and distance > prev_distance:
                            break
           
                # m = (y2 - y1) / (x2 - x1)
                # b = y1 - m * x1
                # prev_y = y1
                # for x in range(x1, x2 + 1):
                #     y = round(m*x + b)
                #    
                #     bitmap[y][x] = 0
                #
                #     if abs(prev_y - y) > 1:
                #         for inter_y in range(prev_y, y):
                #             bitmap[inter_y][x] = 0
                #
                #     prev_y = y
                #

        yield bitmap

if __name__ == "__main__":
    from matplotlib import pyplot as plt
    
    data_set = generate_bitmap("dataset/mushroom.ndjson")
    data = next(data_set)
    
    plt.imshow(data, interpolation='nearest', cmap='gray', vmin=0, vmax=1)
    plt.savefig('output_image.png')
    

                







