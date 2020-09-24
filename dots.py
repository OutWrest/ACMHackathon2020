import numpy as np
from PIL import Image

def dotify(im, inchppx, dist=(3*12), color=(0, 0, 0), dot_width=5, dot_e=10):
    img_arr = np.array(im)
    h, w, _ = (img_arr.shape)

    l = int(dist//inchppx)
    dot_ec = (l//dot_e)

    for col in range((w//l)+1):
        for row in range(h//dot_ec):
            for k in range(dot_width):
                try:
                    img_arr[row*dot_ec + k][(col*l)] = color
                except IndexError:
                    continue
    
    for row in range((h//l)+1):
        for col in range(w//dot_ec):
            for k in range(dot_width):
                try:
                    img_arr[(row*l)][col*dot_ec + k] = color
                except IndexError:
                    continue

    return Image.fromarray(img_arr)

if __name__ == '__main__':
    img = Image.open('CH_3FL.jpg')
    
    # Inner left wall
    # 1461, 58.60ft
    # 1527, 62.01ft

    avg_inpx = (((58.60*12)/1461) + ((62.01*12)/1527))/2
    print(f"Average Inch per Pixel: {avg_inpx}")

    img_dots = dotify(img, avg_inpx, dist=(1*12), dot_e=3, dot_width=3)


    

