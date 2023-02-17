from collections import deque

elf_energies, boxes = deque(list(map(int, input().split()))), deque(list(map(int, input().split())))

turns_count = 0
total_energy_spent = 0
total_boxes = 0

while boxes and elf_energies:
    box = boxes.pop()
    elf_energy = elf_energies.popleft()

    if turns_count % 15 == 0: