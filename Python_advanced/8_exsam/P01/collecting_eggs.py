from collections import deque

SIZE_BOX = 50
eggs = deque([int(el) for el in input().split(", ")])
papers = deque([int(el) for el in input().split(", ")])

boxes = 0

while eggs and papers:
    egg = eggs.popleft()
    if egg <= 0:
        continue
    if egg == 13:
        papers[0], papers[-1] = papers[-1],papers[0]
        continue
    paper = papers.pop()

    if egg + paper <= 50:
        boxes += 1

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if papers:
    print(f"Pieces of paper left: {', '.join([str(x) for x in papers])}")