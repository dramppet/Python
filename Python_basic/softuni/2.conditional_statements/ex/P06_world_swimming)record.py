record_seconds = float(input())
distance = float(input())
time_sec_swimming_for_1_m = float(input())

needed_swimming = distance * time_sec_swimming_for_1_m
add_time = int(distance / 15) * 12.5
needed_time = needed_swimming + add_time

if  needed_time < record_seconds:
    print( f'Yes, he succeeded! The new world record is {needed_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {needed_time - record_seconds:.2f} seconds slower.')