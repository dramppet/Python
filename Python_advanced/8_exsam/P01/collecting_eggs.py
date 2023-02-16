from collections import deque

SIZE_BOX = 50
eggs = deque([int(el) for el in input().split(", ")])
papers = deque([int(el) for el in input().split(", ")])

egg_box = 0
boxes = 0
full_box = False

while eggs and papers:
    egg = eggs.popleft()
    if egg <= 0:
        continue
    if egg == 13:
        papers[0], papers[-1] = papers[-1],papers[0]
        continue
    paper = papers.pop()

    product = egg + paper
    if product + egg_box <= SIZE_BOX:
        egg_box = product
        full_box = True
        boxes += 1
    else:
        egg_box = 0
        continue

if full_box:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if papers:
    print(f"Pieces of paper left: {', '.join([str(x) for x in papers])}")