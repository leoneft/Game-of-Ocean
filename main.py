import numpy as np
import argparse
import os
import time


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("size", help='Size of the ocean: (size x size)', type=int)
    parser.add_argument("e", help='Number of epochs to run', type=int, default=100)
    return parser.parse_args()


def change(a_list, x, y):
    fishes = 0
    shrimps = 0
    if a_list[x][y] == 2 or a_list[x][y] == 3:
        if x != args.size - 1:
            if a_list[x + 1][y] == 2:
                fishes += 1
            if a_list[x + 1][y] == 3:
                shrimps += 1
        if x != 0:
            if a_list[x - 1][y] == 2:
                fishes += 1
            if a_list[x - 1][y] == 3:
                shrimps += 1
        if y != args.size - 1:
            if a_list[x][y + 1] == 2:
                fishes += 1
            if a_list[x][y + 1] == 3:
                shrimps += 1
        if y != 0:
            if a_list[x][y - 1] == 2:
                fishes += 1
            if a_list[x][y - 1] == 3:
                shrimps += 1
        if x != args.size - 1 and y != args.size - 1:
            if a_list[x + 1][y + 1] == 2:
                fishes += 1
            if a_list[x + 1][y + 1] == 3:
                shrimps += 1
        if x != args.size - 1 and y != 0:
            if a_list[x + 1][y - 1] == 2:
                fishes += 1
            if a_list[x + 1][y - 1] == 3:
                shrimps += 1
        if x != 0 and y != args.size - 1:
            if a_list[x - 1][y + 1] == 2:
                fishes += 1
            if a_list[x - 1][y + 1] == 3:
                shrimps += 1
        if x != 0 and y != 0:
            if a_list[x - 1][y - 1] == 2:
                fishes += 1
            if a_list[x - 1][y - 1] == 3:
                shrimps += 1
    if a_list[x][y] == 0:
        if fishes == 3:
            return 2
        elif shrimps == 3:
            return 3
        else:
            return 0
    if a_list[x][y] == 1:
        return 1
    if a_list[x][y] == 2:
        if 2 <= fishes <= 4:
            return 0
        else:
            return 2
    if a_list[x][y] == 3:
        if 2 <= shrimps <= 4:
            return 0
        else:
            return 3


def life(a_list):
    new_ocean = np.zeros((args.size, args.size), dtype=int)
    for i in range(args.size):
        for j in range(args.size):
            new_ocean[i][j] = change(a_list, i, j)
        new_ocean[i] = list(map(int, new_ocean[i]))
    return new_ocean


os.system('cls')
args = parse()
ocean = np.random.randint(0, 4, size=(args.size, args.size))
for row in ocean:
    for elem in row:
        print(elem, end=' ')
    print()
time.sleep(0.5)
os.system('cls')
for epoch in range(args.e):
    ocean = life(ocean)
    os.system('cls')
    for row in ocean:
        for elem in row:
            print(elem, end=' ')
        print()
    time.sleep(0.3)






