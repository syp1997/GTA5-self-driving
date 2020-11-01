import numpy as np
import pandas as pd
from collections import Counter
import random
import warnings
import cv2

warnings.filterwarnings('ignore')

file_name = 'training_data.npy'

training_data = np.load(file_name, allow_pickle=True)

df = pd.DataFrame(training_data)
print(df.head())
print(Counter(df[1].apply(str)))

forwards, lefts, rights = [], [], []

for data in training_data:
    img = data[0]
    move = data[1]
    if move == [1, 0, 0]:
        lefts.append([img, move])
    elif move == [0, 1, 0]:
        forwards.append([img,move])
    elif move == [0, 0, 1]:
        rights.append([img, move])
    else:
        print("No match!!!!")

forwards = forwards[:len(lefts)][:len(rights)]
lefts = lefts[:len(forwards)]
rights = rights[:len(forwards)]

final_data = forwards + lefts + rights

random.shuffle(final_data)
print(len(final_data))
np.save('training_data_v2.npy', final_data)

# for data in training_data:
#     img = data[0]
#     print(img.shape)
#     move = data[1]
#     cv2.imshow('test', img)
#     print(move)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
