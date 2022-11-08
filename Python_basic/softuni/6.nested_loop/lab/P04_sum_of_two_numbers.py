start = int(input())
end = int(input())
magic_num = int(input())

count = 0
is_find = False

for first_d in range(start, end + 1):
    if is_find:
        break
    for sec_d in range(start, end + 1):
        product = first_d + sec_d
        count += 1
        if product == magic_num:
            is_find = True
            print(f'Combination N:{count} ({first_d} + {sec_d} = {magic_num})')
            break
if not is_find:
    print(f'{count} combinations - neither equals {magic_num}')