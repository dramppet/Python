W = 2000
F = 1200
SF = 720

count_tournir = int(input())
point = int(input())

wins = 0
point_win = 0

for _ in range(count_tournir):
    etap = input()

    if etap == 'W':
        wins += 1
        point_win += W
    elif etap == 'F':
        point_win += F
    elif etap == 'SF':
        point_win += SF

print(f'Final points: {point + point_win}')
print(f'Average points: {int(point_win / count_tournir)}')
print(f'{wins / count_tournir * 100:.2f}%')
