def action(pos, des):
    if pos == "left":
        des -= 1
    elif pos == "right":
        des += 1
    else:
        des = des
    return des


position = input()
desk = int(input())

while True:
    if position == 'end':
        break
    print(action(position, desk))
  position = input()
