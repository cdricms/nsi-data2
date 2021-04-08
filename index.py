# # 1

# from typing import SupportsComplex


scores = [
    [511, 542, 532, 531, 555],
    [485, 499, 523, 480, 509],
    [545, 522, 530, 550, 533],
    [516, 462, 502, 498, 487]
]

# print(scores)

# # 2
# print(scores[0])

# # 3
# print(scores[0][2])

# # 4
# print(scores[2][0])

# # 5

# new_scores = scores.copy()
# new_scores[0] = [1, 2, 3, 4, 5]
# new_scores[1][2] = 600
# new_scores[2][3] = 700
# new_scores[3] = [0, 0]

# print(new_scores)


# # 6
# new_scores = scores.copy()
# del new_scores[0][2]
# del new_scores[2][3], new_scores[2][3]
# del new_scores[1]

# print(new_scores)

# # 7
# new_scores = scores.copy()

# new_scores[0].append(600)
# new_scores.insert(2, [0, 0, 0, 0])
# new_scores[3].insert(0, 700)
# new_scores[3].insert(3, 800)
# new_scores[3].append(900)
# new_scores.append([1, 1, 1, 1])

# print(new_scores)

# # 8
# for player_scores in scores:
#     print(player_scores)


# # 9
# for player_scores in scores:
#     for score in player_scores:
#         print(score)

# # 10
# for i in range(len(scores)):
#     print(scores[i], end=", ")

# # 11
# for i in range(len(scores)):
#     for j in range(len(scores[i])):
#         print(scores[i][j], end=", ")

# 12
for col in range(len(scores[0])):
    for row in range(len(scores)):
        print(scores[row][col], end=", ")

for col in range(len(scores)):
    for row in range(len(scores[0])):
        print(scores[col][row], end=", ")


# 13
col = 0
while col < len(scores):
    print(scores[col])
    col += 1

# 14
col = 0
while col < len(scores):
    row = 0
    while row < len(scores[col]):
        print(scores[col][row])
        row += 1
    col += 1


# 15
col = 0
while col < len(scores[0]):
    row = 0
    while row < len(scores):
        print(scores[row][col], end=", ")
        row += 1
    col += 1

row = 0
while row < len(scores):
    col = 0
    while col < len(scores[0]):
        print(scores[row][col], end=", ")
        col += 1
    row += 1

accounts = [
    {"login": "frodon", "password": "mdp123"},
    {"login": "sam", "password": "secret456"},
    {"login": "merry", "password": "psw789"},
    {"login": "pippin", "password": "1234"},
]

# 16
print(accounts)

# 17
print(accounts[2])

# 18
print(accounts[1]["password"])

# 20
accounts[0]["login"], accounts[0]["password"] = "frodon-sacquet", "mon_précieux"
accounts[2]["login"] = "meriadoc"
accounts[3]["password"] = "abcd"

# 21
del accounts[3]

# 22
accounts.insert(2, {"login": "bilbon", "password": "cul-de-sac"})
accounts.append({"login": "gandalf", "password": "gripoil"})


# 23
for account in accounts:
    print(account)

# 24
for account in accounts:
    for val in account.values():
        print(val)

# 25
for account in accounts:
    for key, val in account.items():
        print(f"{key}: {val}", end=" // ")
