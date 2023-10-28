import numpy as np

BITMAP_SIZE = 256

def generate_bitmap(ndjson_generator):
    for json_obj in ndjson_generator:
        # create 2D array
        bitmap = np.ones((BITMAP_SIZE, BITMAP_SIZE), dtype=float)

        strokes = json_obj["drawing"]

        # go through the strokes
        for stroke in strokes:
            # get each point in the stroke
            x_vals = stroke[0]
            y_vals = stroke[1]

            for point_num in range(len(x_vals) - 1):
                x1, y1 = x_vals[point_num], y_vals[point_num]
                x2, y2 = x_vals[point_num + 1], y_vals[point_num + 1]

                if x1 == x2:
                    for y in range(y1, y2, 2 * (x1 < x2) - 1):
                        bitmap[y][x1] = 0
                    continue

                m = (y2 - y1) / (x2 - x1)
                b = y1 - m * x1
                prev_y = y1
                for x in range(x1, x2 + 1, 2 * (x1 < x2) - 1):
                    y = round(m*x + b)
                    
                    bitmap[y][x] = 0

                    if abs(prev_y - y) > 1:
                        for inter_y in range(prev_y, y, 2 * (x1 < x2) - 1):
                            bitmap[inter_y][x] = 0

                    prev_y = y


        yield bitmap

if __name__ == "__main__":
    from read_data import get_data
    from matplotlib import pyplot as plt

    data_set = generate_bitmap(get_data("dt23_dataset/mushroom.ndjson"))
    data = next(data_set)
    data = next(data_set)

    plt.imshow(data, interpolation='nearest', cmap='gray', vmin=0, vmax=1)
    plt.savefig('output_image.png')

                







