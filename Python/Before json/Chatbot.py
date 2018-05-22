import json
import time
## Input some data
def inputData(orders):
    while True:
        name = input("Name?")
        if name =="":
            break
        choice = input("Menu Choice?")
        orders[name]=choice
    return orders
#Store it in a file
def storeData(orders):
    with open("data.txt", 'w') as f:
        json.dump(orders, f)
        
#Get it from file
def getData():
    try:
        with open("data.txt", 'r') as f:
            orders = json.load(f)
    except FileNotFoundError: 
        orders = {} #Empty Dictionary

    return orders

#Display contents
def displayData(orders):
    print(orders)
 
 
getData()

print("Hi, my name is OB7026 - a food-ordering bot - and I'll be serving you today.")
#Introduction
while True:
    time.sleep(2)
    intro = input('What would you like? ')
    if intro == 'I want food' or intro == 'I want to order food' or intro == 'i want food' or intro == 'i want to order food':
        time.sleep(1)
        print("Great")
        break
    time.sleep(0.75)
    print("Sorry, I don't understand. Could you please repeat? ")
#Input Name
yourname = []
time.sleep(0.5)
name = input('What is your name? ')
while 'my name is' not in name:
    time.sleep(2)
    print("Sorry, I don't understand. Could you please repeat? ")
    time.sleep(0.5)
    name = input("What is your name? ")
else:
    name = name.replace('my name is', '')
time.sleep(1)
confirm = input('Your name is' + name.title() + '? ')
while confirm == 'no':
    time.sleep(2)
    print('Sorry I got that wrong.')
    time.sleep(2)
    name = input("Please tell me your name. ")
    name = name.replace("my name is", "")
    time.sleep(1)
    confirm = input("Your name is "+ "" +name.title() + '? ')
else:
    name = name.replace("my name is", "")
    time.sleep(1)
    yourname.append(name)
    print("Welcome," + name.title()+".")
    
#Ask For Menu
choices = []
menu = {
            "pizza" : 11.50,
            "chicken strips" : 12.00,
            "hamburger" : 9.00,
            "churros" :  5.00,
            "burrito" : 8.00
        }
count = 1
totalcost=0
while True:
    time.sleep(2)
    wantmenu = input("Would you like to see our menu? ")
    if "Yes" in wantmenu or "yes" in wantmenu:      
#Print Menu        
        time.sleep(1)
        print('Here you are...')
        time.sleep(2)
        
        
        print()
        print("   ---Menu---")
        for item in menu:
            price = menu[item]
            print(f"[ {item} - ${price}0 ]")
            print("   ----------")
            count += 1
        print()
#Ordering        
        while True:
            time.sleep(0.75)
            order = input("What would you like to eat? ").lower().strip()
            if order=="":
                if len(choices)>= 3:
                    time.sleep(0.5)
                    confirmchoices=input('Would you like to order more? ')
                    if confirmchoices != 'yes':
                        time.sleep(0.5)
                        print()
                        print('Thanks for ordering with us. You order has been saved.')
                        print(f'Your total comes out to ${totalcost}0.')
                        input('PRESS ENTER TO HANG UP THE PHONE')
                        exit()
                else:
                    print()
                    time.sleep(0.5)
                    print("You don't have enough orders for delivery. Please order at least 3 items.")
                    continue        
            if order in menu:
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
#If Not Viewing Menu             
    else:
        while True:
            time.sleep(0.75)
            order = input("What would you like to eat? ").lower().strip()
            if order=="":
                if len(choices)>= 3:
                    time.sleep(0.5)
                    confirmchoices=input('Would you like to order more? ')
                    if confirmchoices != 'yes':
                        time.sleep(0.5)
                        print()
                        print('Thanks for ordering with us. You order has been saved.')
                        print(f'Your total comes out to ${totalcost}0.')
                        input('PRESS ENTER TO HANG UP THE PHONE')
                        exit()
                else:
                    print()
                    time.sleep(0.5)
                    print("You don't have enough orders for delivery. Please order at least 3 items.")
                    continue        
            if order in menu:
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