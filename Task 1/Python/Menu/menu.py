menu = {
	"pizza" : 3.40,
	"tacos" : 5.60,
	"curry chicken": 13.00
}

print("Menu")
count = 1
for item in menu:
	price = menu[item]
	print(f"> {item} - ${price}")
	count += 1
totalcost=0
while True:
	order = input("What would you like to eat?").lower().strip()
	if order =="":
		break
	if order in menu:
		cost = menu[order]
		totalcost += cost
		print(f"Thank you for ordering - {order}, that will cost {cost}, and your total is now {totalcost}.")
	else:
		print(f"{order} is not on the menu. Please choose something else.")