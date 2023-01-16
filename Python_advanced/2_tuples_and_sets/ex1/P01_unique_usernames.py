count_usernames = int(input())
unique_users = set()

for _ in range(count_usernames):
    unique_users.add(input())

print('\n'.join(unique_users))