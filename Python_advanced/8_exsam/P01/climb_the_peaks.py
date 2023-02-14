from collections import deque


def climb_peaks(food_portions, stamina_day):
    food_portions, stamina_day = deque(), deque()

    energy_need_day = food_portions.pop() + stamina_day.popleft()

    mountain_peaks = {'Vihren': 80, 'Kutelo': 90, 'Banski Suhodol': 100, 'Polezhan': 60, 'Kamenitza': 70}


food = list(map(int, input().split(", ")))
stamina = list(map(int, input().split(", ")))
