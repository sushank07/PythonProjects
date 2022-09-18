# import random

# r=['1','2','3']

# while True:
#     you=input("select 1:stone 2:paper 3:scissor :")
#     print(f"you select {you}")
#     computer=random.choice(r)
#     print(f"computer select {computer}")

#     if you=='1' and computer=='2':
#         print("computer win")
    
#     elif you=='1' and computer=='3':
#         print("you win")

#     elif you=='2' and computer=='1':
#         print("you win")

#     elif you=='2' and computer=='3':
#         print("computer win")

#     elif you=='3' and computer=='1':
#         print("computer win")

#     elif you=='3' and computer=='2':
#         print("you win")

#     elif you==computer:
#         print("tie")

#     else:
#         print(" ")


import random
while True:
    you=input("enter your choice [stone , paper , scissor]\n")
    comp=["stone","paper","scissor"]
    computer=random.choice(comp)
    if you==computer:
        print(f"you choose {you} computer choose {computer} its tie\n")
    elif you=="stone":
        if computer=="scissor":           
            print("you choose stone & computer choose scissor ! you win\n")
        else:
            print("you choose stone & computer choose paper ! computer win\n")
    
    elif you == "paper":
        if computer=="stone":
            print("you choose paper & computer choose stone ! you win\n")
        else:
            print("you choose paper & computer choose scissor ! computer win\n")

    elif you=="scissor":
        if computer=="paper":
            print("you choose scissor & computer choose paper ! you win\n")
        else:
            print("you choose scissor & computer choose stone ! computer win\n")
        

    























