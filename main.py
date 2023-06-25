from data import data
from logoandVs import vs,logo
import random
import os

a_account = random.choice(data)
b_account = random.choice(data)
score = 0
isUserTrue = True




def random_formate(account):
    account_name = account["name"]
    # account_follwer = account["follower_count"]
    account_discr = account["description"]
    account_con = account["country"]
    return f"{account_name} a {account_discr} and from {account_con} ."

# print(a_account)
# print(b_account)

# compare the follower
while isUserTrue:
    b_account_follower = b_account["follower_count"]

    a_account_follower = a_account["follower_count"]
    if a_account == b_account:
        b_account = random.choice(data)
    print(logo)
    # print(random_formate())
    print(f"A compare {random_formate(a_account)}")
    print(vs)
    print(f"B compare {random_formate(b_account)}")

    user = input("Who has more follower 'A' or 'B'").lower()
    os.system('clear')
    if user == "a" and a_account_follower >b_account_follower:
        # print("print yes")
        a_account = random.choice(data)
        score +=1
    elif user == "b" and b_account_follower >a_account_follower:
        b_account = random.choice(data)
        score +=1
    else:
        isUserTrue = False
        print(f"You loose your total score is {score}")
# print(score)    