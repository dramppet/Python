from collections import deque

elf_energies, boxes = deque(list(map(int, input().split()))), deque(list(map(int, input().split())))

turns_count = 0
total_energy_spent = 0
toys_count = 0

while boxes and elf_energies:
    while elf_energies and elf_energies[0] < 5:
        elf_energies.popleft()

    if not elf_energies:
        break

    toys_count += 1
    box = boxes.pop()
    elf_energy = elf_energies.popleft()

    if turns_count % 15 == 0 and (2 * box) <= elf_energy:
        total_energy_spent += 2 * box
        elf_energies.append(elf_energy - (2 * box))
    elif turns_count % 5 == 0 and box <= elf_energy:
        total_energy_spent +=  box
        elf_energies.append(elf_energy - box)
    elif turns_count % 3 == 0 and (2 * box) <= elf_energy:
        toys_count += 2
        total_energy_spent += 2 * box
        elf_energies.append(elf_energy - (2 * box) + 1)
    elif box <= elf_energy:
        toys_count += 1
        total_energy_spent += 1 * box
        elf_energies.append(elf_energy - box + 1 )
    else:
        boxes.append(box)
        elf_energies.append(elf_energy * 2)

print(f"Toys: {toys_count}")
print(f"Energy: {total_energy_spent}")

if elf_energies:
    print(f"Elves left: {', '.join([str(x) for x in elf_energies])}")

if boxes:
    print(f"Boxes left: {', '.join([str(x) for x in boxes])}")
