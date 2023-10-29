from read_data import get_data
import numpy as np
import math

BITMAP_SIZE = 256
STROKE_RADIUS = 5

def distance_line(x, y, start_point, end_point):
    # find distance
    line_vec = end_point - start_point
    point_vec = np.array([x, y]) - start_point
    projection = (point_vec @ line_vec) * line_vec / (line_vec @ line_vec)
    point = projection + start_point

    # check if point within the line segment
    if point[0] < start_point[0]:
        distance = math.sqrt(point_vec @ point_vec)
    elif point[0] > end_point[0]:
        distance = math.sqrt((end_point[0] - x) ** 2 + (end_point[1] - y) ** 2)
    else:
        # along the line
        distance_vec = point_vec - projection
        distance = math.sqrt(distance_vec @ distance_vec)

    return distance



def generate_bitmap(filename):
    for json_obj in get_data(filename):
        # create 2D array
        bitmap = np.ones((BITMAP_SIZE, BITMAP_SIZE), dtype=bool)

        strokes = json_obj["drawing"]

        # go through the strokes
        for stroke in strokes:
            # get each point in the stroke
            x_vals = stroke[0]
            y_vals = stroke[1]

            for point_num in range(len(x_vals) - 1):
                x1, y1 = x_vals[point_num], y_vals[point_num]
                x2, y2 = x_vals[point_num + 1], y_vals[point_num + 1]

                if x2 < x1:
                    x1, x2, y1, y2 = x2, x1, y2, y1

                start_x = max(x1 - STROKE_RADIUS, 0)
                final_x = min(x2 + STROKE_RADIUS, BITMAP_SIZE - 1)
                start_y = max((y1 if y1 < y2 else y2) - STROKE_RADIUS, 0)
                final_y = min((y2 if y1 < y2 else y1) + STROKE_RADIUS, BITMAP_SIZE - 1)

                start_point = np.array([x1, y1])
                end_point = np.array([x2, y2])
                
                for y in range(start_y, final_y):
                    prev_distance = 0
                    distance = 0

                    for x in range(start_x, final_x):
                        prev_distance = distance
                        distance = distance_line(x, y, start_point, end_point)
                        if distance <= STROKE_RADIUS:
                            bitmap[y][x] = 0
                        elif prev_distance != 0 and distance > prev_distance:
                            break

        yield bitmap

if __name__ == "__main__":
    from matplotlib import pyplot as plt
    
    data_set = generate_bitmap("dataset/mushroom.ndjson")
    data = next(data_set)
    
    plt.imshow(data, interpolation='nearest', cmap='gray', vmin=0, vmax=1)
    plt.savefig('output_image.png')


    

                







