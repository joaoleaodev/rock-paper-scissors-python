import random
import time

rps = ["r", "p", "s"]
my_points = 0
pc_points = 0
print("You need to choose one! R is for rock, P for paper and S for scissors")
time.sleep(2)
print("The game is about to start...")
time.sleep(1)
number = 3

while number: 
    print(f"{number}")
    time.sleep(1)
    number -= 1 
print("GOOD LUCK !")
time.sleep(1)

while my_points <2 and pc_points <2:
    your_play = input("Your play: ").lower()
    if your_play not in rps:
        print("Invalid option! Choose r, p or s \n")
        continue
    pc_play = random.choice(rps)
    print(f"PC played: {pc_play}")
    
    if your_play == "r" and pc_play == "s":
        print("You won this round!")
        my_points += 1
        print(f"The score is:\nYou: {my_points}\nPC: {pc_points}\n")
    elif your_play == "p" and pc_play == "r":
        print("You won this round!")
        my_points += 1
        print(f"The score is:\nYou: {my_points}\nPC: {pc_points}\n")
    elif your_play == "s" and pc_play == "p":
        print("You won this round!")
        my_points += 1
        print(f"The score is:\nYou: {my_points}\nPC: {pc_points}\n")
    elif your_play == "r" and pc_play == "p":
        print("PC won this round!")
        pc_points += 1
        print(f"The score is:\nYou: {my_points}\nPC: {pc_points}\n")
    elif your_play == "s" and pc_play == "r":
        print("PC won this round!")
        pc_points += 1
        print(f"The score is:\nYou: {my_points}\nPC: {pc_points}\n")
    elif your_play == "p" and pc_play == "s":
        print("PC won this round!")
        pc_points += 1
        print(f"The score is:\nYou: {my_points}\nPC: {pc_points}\n")
    elif your_play == pc_play:
        print("Oh! Thats a tie! Let's go for another round")
        print(f"The score is:\nYou: {my_points}\nPC: {pc_points}\n")

if my_points > pc_points:
    print("👤 You won the game!")
else:
    print("💻 PC won the game!")
