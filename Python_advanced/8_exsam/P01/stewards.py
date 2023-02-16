from collections import deque

seats = input().split(", ")
first_numbers = deque(list(map(int, input().split(", "))))
second_numbers = deque(list(map(int, input().split(", "))))

taken_seats = []
rotations = 0

while rotations < 10 and len(taken_seats) < 3:
    rotations += 1

    first_num = first_numbers.popleft()
    second_num = second_numbers.pop()

    letter = chr(first_num + second_num)

