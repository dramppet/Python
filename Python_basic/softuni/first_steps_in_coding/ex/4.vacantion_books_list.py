count_pages = int(input())
pages_for_one_hours = int(input())
count_days = int(input())

all_time_reads_books = int(count_pages / pages_for_one_hours)
need_hours_day = int(all_time_reads_books / count_days)

print(need_hours_day)