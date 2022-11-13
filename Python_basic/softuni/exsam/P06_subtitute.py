K = int(input())
L = int(input())
M = int(input())
N = int(input())

smeni = 0
is_break = False

# if K > 8:
#     K = 8
# if K < 0:
#     K = 0
# if L > 9:
#     L = 9
# if L < 0:
#     L = 0
# if M > 8:
#     M = 8
# if M < 0:
#     M = 0
# if N > 9:
#     N = 9
# if N < 0:
#     N = 0

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

