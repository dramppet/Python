import sys

max_H = 0
index = 0

while True:

    for i in range(8):
        mounth_h = int(input())

        if mounth_h > max_H:
            max_H = mounth_h
            index = i
    max_H = 0

    print(index)

