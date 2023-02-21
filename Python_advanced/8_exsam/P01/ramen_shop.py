from collections import deque

ramen_bowls, customers = deque(list(map(int, input().split(", ")))), deque(list(map(int, input().split(", "))))

while customers:
    if not ramen_bowls:
        print("Out of ramen! You didn't manage to serve all customers.")
        print(f"Customers left: {', '.join((map(str,customers)))}")
        break
    customer = customers.popleft()
    bow = ramen_bowls.pop()

    if customer > bow:
        customers.appendleft(customer - bow)
    elif customer < bow:
        ramen_bowls.append(bow - customer)
else:
    print('Great job! You served all the customers.')
    if ramen_bowls:
        print(f"Bowls of ramen left: {', '.join((map(str, ramen_bowls)))}")





