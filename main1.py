#!/usr/bin/python3
class shop:
	_console=True
	drinks={"item": [], "cost":[], "count":0}
	food={"item": [], "cost": [], "count":0 }
	other={"item": [], "cost": [], "count":0}
	def add_item(key,i,c):
		key["item"].append(i)
		key["cost"].append(c)
		key["count"] += 1
	def list_out(key):
		for each in range(key["count"]):
			print("Item: %s | Cost: %f"%(key["item"][each],key["cost"][each]))
shop.add_item(shop.drinks,"Monster Energy Drink",1.55)
shop.add_item(shop.drinks,"Beer",5.00)
shop.add_item(shop.drinks,"Fruit-juice",2.00)
shop.add_item(shop.food,"Pizza",5.00)
shop.add_item(shop.food,"Cake",5.00)
shop.add_item(shop.food,"Bacon",2.00)
def str_info(arg):
	print("%s"%(arg))
	return str(input("> "))
def int_info(arg):
	print("%s"%(arg))
	return int(input("> "))
def float_info(arg):
	print("%s"%(arg))
	return float(input("> "))
def console(arg):
	cmdlist=["help: This help menu.", "add_food: Tells the console to add a food item and a price for it.",
	"add_drink: Tells the console to add a drink item and a price for it.",
	"add_other: Tells the console to add another type of item with a price."
	"list_out: Tells the console to list out a spesific list."]
	if arg == "add_drink":
		drink_item=str_info("Drink item please: "); drink_cost = float_info("The price of this drink item please.")
		shop.add_item(shop.drinks,drink_item,drink_cost)
	elif arg == "add_food":
		food_item=str_info("Food item please."); food_cost = float_info("The price of this food item please.")
		shop.add_item(shop.food,food_item,food_cost)
	elif arg == "add_other":
		other_item=str_info("Any type of item please: "); other_cost = float_info("The price of this 'other' please.")
	elif arg == "list_out":
		list_out=str_info("Please give me a list name of 'food','drink' or 'other'.")
		if list_out == "food":
			shop.list_out(shop.food)
		elif list_out == "drink":
			shop.list_out(shop.drinks)
		elif list_out == "other":
			shop.list_out(shop.other)
		else:
			print("No idea, sorry!")
	elif arg == "help":
		for each in cmdlist:
			print("%s"%(each))
	elif arg == "exit":
		print("See you, then!")
		shop._console = False
while 1 and shop._console:
	console(str_info("A command please(not sure?'help' may help.)."))
