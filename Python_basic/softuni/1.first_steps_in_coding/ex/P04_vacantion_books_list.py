count_pages = int(input())
pages = int(input())
count_day = int(input())

read_time = count_pages / pages
need_hours_day = read_time / count_day

print(int(need_hours_day))