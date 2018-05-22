import json
orders = {
    'zac' : ["tacos","pizza"],
    'cian' : ['babyfood','mush']
}

for person in orders:
    choices = orders[person]
    print(f"{person} has ordered:")
    for orderList in choices:
        print("====")    
        for item in orderList:
            print(item)