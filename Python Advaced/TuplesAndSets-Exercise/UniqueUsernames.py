number = int(input())
usernames = set()

for u in range(number):
    username = input()
    usernames.add(username)

for username in usernames:
    print(username)