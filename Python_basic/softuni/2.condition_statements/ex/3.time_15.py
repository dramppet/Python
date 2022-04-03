minute_input = int(input())
seconds_input = int(input())

seconds = seconds_input + 15

if seconds > 60:
    minute_input += 1
    seconds = seconds % 60
    if minute_input < 24:
        if seconds < 10:
            print(f'{minute_input}:0{seconds}')
        else:
            print(f'{minute_input}:{seconds}')
    else:
        pass

else:
    print(f'{minute_input}:{seconds}')


