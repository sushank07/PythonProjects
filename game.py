from random import *
r=['1','2','3']

while True:
    you=input("select 1:stone 2:paper 3:scissor :")
    print(f"you select {you}")
    computer=choice(r)
    print(f"computer select {computer}")

    if you=='1' and computer=='2':
        print("computer win")
    
    elif you=='1' and computer=='3':
        print("you win")

    elif you=='2' and computer=='1':
        print("you win")

    elif you=='2' and computer=='3':
        print("computer win")

    elif you=='3' and computer=='1':
        print("computer win")

    elif you=='3' and computer=='2':
        print("you win")

    elif you==computer:
        print("tie")

    else:
        print(" ")