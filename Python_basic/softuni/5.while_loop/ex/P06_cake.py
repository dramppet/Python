total_pieces = int(input()) * int(input())
pieces_eaten = 0

while total_pieces >= pieces_eaten:
    pieces = input()

    if pieces == 'STOP':
        print(f'{total_pieces - pieces_eaten} pieces are left.')
        break

    pieces_eaten += int(pieces)

else:
    print(f'No more cake left! You need {pieces_eaten - total_pieces} pieces more.')

