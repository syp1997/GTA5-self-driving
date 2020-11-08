import numpy as np
import cv2
import time
import os
from grab_screen import grab_screen
from get_keys import key_check


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def keys_output(keys):
    output = [0, 0, 0]

    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1

    return output


file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('Loading previous data!')
    training_data = list(np.load(file_name, allow_pickle=True))
else:
    print('Starting fresh!')
    training_data = []


def main():
    for i in list(range(3))[::-1]:
        print(i + 1)
        time.sleep(1)
    last_time = time.time()
    while True:
        screen = grab_screen(region=(0,40,800,640))
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
        screen = cv2.resize(screen, (80,60))
        keys = key_check()
        output = keys_output(keys)
        training_data.append([screen, output])
        print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()

        if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_name, training_data)


# main()
