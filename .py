import time

# Start of game
while True:
    answer = input("Do you want to play (yes/no)")
    if answer == "yes":
        break
    else:
        print("Cmon just play the game!")

print("Ok lets get started")
print("You walked into the forest..")
time.sleep(2)

# path 1 or 2
while True:
    path_option = input("There are 2 paths \n Which path will you pick \n path 1 path 2")

    if path_option == "path 1" or path_option == "path 2":
        break

if path_option == "path 1":
    time.sleep(1)

    print("You found a chest!")

    time.sleep(2)

    print("You open the chest and found a hat \n you kept the hat")

    time.sleep(1)


    print("You saw a guy in need in help")
    time.sleep(3)

    while True:
        help = input("Would you like to help (yes/no)?")
        if help == "yes" or help == "no":
            break
    if help == "yes":

        print("You helped him")
        time.sleep(1)

        print("You and Zach are now buddys!")
        time.sleep(2)

    elif help == "no":
        print("You left him alone")



# bear part/ path 2
elif path_option == "path 2":
    time.sleep(1)

    print("You encountered a large bear")

    while True:
        attackOrNo = input("Do you want to attack (yes/no)")
        if attackOrNo == "yes" or attackOrNo == "no":
            break

    if attackOrNo == "yes":
        time.sleep(2)
        print("The bear was stronger than you \n so you ran away")
        time.sleep(2)
        print("You continued to walk")
        break
#Old Man       
time.sleep(2)
print("You found an old man")
time.sleep(1)
print("You decided to talk to him")
time.sleep(3)
print("Old man: 'Hey there sunny need any help?")
time.sleep(1)
print("You: 'Yes I need to know the path to the mountians")
time.sleep(1)
print("Old man: 'Hmm? Seems like explaining will be harder'")
print("Old man: 'Come, I will walk with you there'")
time.sleep(3)

print("NARATOR: So you and the old man went through a journey to the mountains")
time.sleep(2)
print("The end...")

    elif attackOrNo == "no":
        time.sleep(2)
        print("You decided to walk away")
        time.sleep(2)
        print("You continued to walk")
