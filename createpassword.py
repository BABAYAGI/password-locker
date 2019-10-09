# import pickle
# import random

# info = {}

# with open("game.p", "br") as readfile:
#   info = pickle.load(readfile)
# print(info)
# s = "QWERTYUIOPLKJHGFDSAZXCVBNM,.;'[]=-qwertyuioplkjhgfdsazxcvbnm,.;']*-1234567890!@##$%^&*()_+"
# len_password = int(input("enter number of characters in password :"))
# password = "".join(random.sample(s, len_password))
# print(password)

# answer = input("would you like to keep this password y:")
# if ("y" in answer):
#     account_name = input("enter account name:")
#     info[account_name] = password
#     print(info)
#     with open("game.p", "bw") as filewrite:
#         pickle.dump(info, filewrite, protocol=2)

# else:
#     print("ok")
