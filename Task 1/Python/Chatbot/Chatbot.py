import json
import time

orders = {} #Empty Dictionary
menu = {
            "pizza" : 11.50,
            "chicken strips" : 12.00,
            "hamburger" : 9.00,
            "churros" :  5.00,
            "burrito" : 8.00
        }

def getOrders(name):
    chocies = []
    pastOrders = getPastOrders(name)
    while True:
        choice = input("What ?")
        choices.append(choice)
        
    pastOrders.append(choices)
#-------------------------------------------------------------
def storeData(orders):
    with open("orders.txt", 'w') as f:
        json.dump(orders, f)

#-------------------------------------------------------------
def getName():
    name = input('What is your name? ').lower()
    while 'my name is' not in name:
        time.sleep(0.75)
        print("Sorry, I don't understand. Could you please repeat? ")
        time.sleep(0.5)
        name = input("What is your name? ").lower()
    else:
        name = name.replace('my name is', '').lower()
    time.sleep(1)
    confirm = input('Your name is' + name.title() + '? ').lower()
    while confirm == 'no':
        time.sleep(0.75)
        print('Sorry I got that wrong.')
        time.sleep(0.5)
        name = input("Please tell me your name. ").lower()
        name = name.replace("my name is", "").lower()
        time.sleep(1)
        confirm = input("Your name is "+ "" +name.title() + '? ').lower()
        
    else:
        name = name.replace("my name is", "").lower()
        time.sleep(1)
        print("Welcome," + name.title()+".")
    return name

#-------------------------------------------------------------
def printMenu():
    time.sleep(1)
    print('Here you are...')
    time.sleep(2)
       
    print()
    print("   ---Menu---")
    for item in menu:
        price = menu[item]
        print(f"[ {item} - ${price}0 ]")
        print("   ----------")
    print()

#-------------------------------------------------------------
def menuOrderTime():
    
    choices = []
    totalcost=0
    while True:
        time.sleep(0.75)
        order = input("What would you like to eat? ").lower().strip()
        orders[name]=choices
        if order=="":
            if len(choices)>= 3:
                time.sleep(0.5)
                confirmchoices=input('Would you like to order more? ').lower()
                if confirmchoices != 'yes':
                    time.sleep(0.5)
                    print()
                    print('Thanks for ordering with us. You order has been saved.')
                    print(orders)
                    storeData(orders)
                    print(f'Your total comes out to ${totalcost}0.')
                    input('PRESS ENTER TO HANG UP THE PHONE')
                    exit()
            else:
                print()
                time.sleep(0.5)
                print("You don't have enough orders for delivery. Please order at least 3 items.")
                continue        
        elif order in menu:
            cost = menu[order]
            choices.append(order)
            totalcost += cost
            time.sleep(0.5)
            print()
            print(f"{order} has been added to your orders, that will cost ${cost}0. Your total is now ${totalcost}0.")
            print('PRESS ENTER WHEN READY TO COMPLETE YOUR ORDER')
        else:
            time.sleep(0.5)
            print(f"{order} is not on the menu. Please choose something else.")
#-------------------------------------------------------------
def inputData(orders):
        
    #first get the name

    #Ask For Menu
    while True:
        time.sleep(2)
        wantmenu = input("Would you like to see our menu? ").lower()
        if wantmenu.lower() == 'yes':
            printMenu()
            menuOrderTime()
        elif wantmenu.lower() == 'no':
            menuOrderTime()                                    
        else:
            time.sleep(0.5)
            print("Sorry, I don't understand.")
            continue
#==================================================================
#MAIN PRGOGRAM

print("Hi, my name is OB7026 - a food-ordering bot - and I'll be serving you today.")
#Introduction
while True:
    time.sleep(2)
    intro = input('What would you like? ').lower()

    if intro == 'i want food' or intro == 'i want to order food':
        time.sleep(1)
        print("Great")
        break
    time.sleep(0.75)
    print("Sorry, I don't understand. Could you please repeat? ")
#Input Name & Order Menu
time.sleep(0.5)
name = getName()
inputData(orders)
                                                                     