from collections import deque


def climb_peaks(food_portions, stamina_day):
    food_portions, stamina_day = deque(food_portions), deque(stamina_day)


    mountain_peaks = {'Vihren': 80, 'Kutelo': 90, 'Banski Suhodol': 100, 'Polezhan': 60, 'Kamenitza': 70}

    climb_peak = []
    faled = False

    for peak, difficulty_level in mountain_peaks.items():

        while True:
            energy_need_day = food_portions.pop() + stamina_day.popleft()

            if energy_need_day >= difficulty_level:
                climb_peak.append(peak)
                break
            elif (len(food_portions) == 0 or len(stamina_day) == 0) :
                    faled = True
                    break
    else:
        if faled:
            if len(climb_peak) == 0:
                return 'Alex failed! He has to organize his journey better next time -> @PIRINWINS'
            else:
                data_rep = '\n'.join(climb_peak)
                return f'Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK\nConquered peaks:\n{data_rep}'

        data_rep = '\n'.join(climb_peak)
        return f'Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK\nConquered peaks:\n{data_rep}'


food = list(map(int, input().split(", ")))
stamina = list(map(int, input().split(", ")))

print(climb_peaks(food,stamina))
