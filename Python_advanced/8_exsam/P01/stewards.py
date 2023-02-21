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

    first_option = str(first_num) + letter
    second_option = str(second_num) + letter

    if first_option in taken_seats or second_option in taken_seats:
        continue

    if first_option in seats:
        taken_seats.append(first_option)
        continue
    if second_option in seats:
        taken_seats.append(second_option)
        continue

    first_numbers.append(first_num), second_numbers.appendleft(second_num)

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")




