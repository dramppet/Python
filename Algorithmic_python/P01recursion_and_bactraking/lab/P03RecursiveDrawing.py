def draw_figura(n):
    if n == 0:
        return
    print('*' * n)
    draw_figura(n - 1)
    print('#' * n)

n = int(input())
draw_figura(n)
