K = int(input())
L = int(input())
M = int(input())
N = int(input())

smeni = 0
is_break = False

for k in range(K, 9):
    if is_break:
        break
    for l in range(9, L - 1, -1):
        for m in range(M, 8 + 1):
            if is_break:
                break
            for n in range(9, N - 1, -1):
                if (k % 2 == 0 and l % 2 == 1) and (m % 2 == 0 and n % 2 == 1):
                    if f'{k}{l}' == f'{m}{n}':
                        print('Cannot change the same player.')
                    else:
                        print(f'{k}{l} - {m}{n}')
                        smeni += 1
                if smeni >= 6:
                    is_break = True
                    break

