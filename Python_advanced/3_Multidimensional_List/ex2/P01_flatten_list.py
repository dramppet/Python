line = input().split("|")

sub_list = []

for sub_str in line[::-1]:
    sub_list.extend(sub_str.split())

print(*sub_list,sep=" ")
