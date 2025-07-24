import time
#Baking sim

inv = []
upgrades = []

cookSpeed = 1

#recipes:

dabloons = 0

def Load(type):
    if type == "cooking":
        print("cooking.")
        time.sleep(cookSpeed)
        print("cooking..")
        time.sleep(cookSpeed)
        print("cooking...")
        time.sleep(cookSpeed)

def Sell(food):
    global dabloons
    if food == "bread":
        if "bread" in inv:
            inv.remove("bread")
            print("sold bread || + 1 dabloons")
            dabloons += 1
        else:
            print("No bread in inventory!")
    if food == "dough":
        if "dough" in inv:
            inv.remove("dough")
            print("sold dough || + 0.5 dabloons")
            dabloons += 0.5
        else:
            print("No bread in inventory!")

def Upgrade(type):
    if type == "cook speed"

while True:
    ingred = input("?:  ")
    if ingred == "cook":
        if "dough" in inv:
            Load(type = "cooking")
            print("bread")
            inv.remove("dough")
            inv.append("bread")
            #print(ingred)
    if ingred == "sell":
        x = input("what do you want to sell?  ")
        Sell(food = x)
    if ingred == "upgrade":
        x = input("what do you want to upgrade?  ")
        if x == "cook speed":
            cookSpeed -= 0.5
            print("Cooking speed has decreased -0.5 seconds")
    if ingred == "inv":
        print(inv, "<<< Stash")
        print(dabloons, "dabloons")
    if ingred == "dough":
        inv.append("dough")
    
    if ingred == "end":
        break

