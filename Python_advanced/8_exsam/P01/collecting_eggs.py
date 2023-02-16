from collections import deque

SIZE_BOX = 50
eggs = deque([int(el) for el in input().split(", ")])
piece_of_paper = deque([int(el) for el in input().split(", ")])

egg_box = 0
box = 0
full_box = False

while True:
    if len(eggs) == 0:
        break
    if len(piece_of_paper)  == 0:
        break
    egg = eggs.popleft()
    if egg <= 0:
        continue
    if egg == 13:
        a = piece_of_paper.popleft()
        b = piece_of_paper.pop()

        a,b = piece_of_paper.append(a),piece_of_paper.appendleft(b)
    paper = piece_of_paper.pop()

    product = egg + paper
    if product + egg_box <= SIZE_BOX:
        egg_box = product
        full_box = True
        box += 1
    else:
        egg_box = 0
        continue

if full_box:
    print(f"Great! You filled {box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if piece_of_paper:
    print(f"Pieces of paper left: {', '.join([str(x) for x in piece_of_paper])}")