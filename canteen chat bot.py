class CitCanteenBot:
    def __init__(self):
        self.food_menu = {'Burger': 50, 'Pizza': 100, 'Pasta': 80, 'Sandwich': 30,'Tea':10,'Coffee':10,'Fries':40,'Briyani':100,'Bonda':15}
        self.order = {}

    def display_menu(self):
        print("Here's our menu:")
        for food, price in self.food_menu.items():
            print(f"{food} - {price}")

    def add_to_order(self, food, quantity):
        if food in self.food_menu:
            self.order[food] = self.order.get(food, 0) + quantity
            print(f"{quantity} {food}(s) added to your order.")
        else:
            print("Sorry, we don't have that in our menu.")

    def remove_from_order(self, food, quantity):
        if food in self.order:
            if self.order[food] >= quantity:
                self.order[food] -= quantity
                print(f"{quantity} {food}(s) removed from your order.")
                if self.order[food] == 0:
                    del self.order[food]
            else:
                print(f"We don't have {quantity} {food}(s) in your order.")
        else:
            print(f"{food} is not in your order.")

    def modify_order(self, food, quantity):
        if food in self.food_menu:
            if quantity > 0:
                self.order[food] = quantity
                print(f"Your order for {food} has been modified to {quantity}.")
            else:
                del self.order[food]
                print(f"{food} has been removed from your order.")
        else:
            print("Sorry, we don't have that in our menu.")

    def view_order(self):
        if self.order:
            print("Your current order:")
            for food, quantity in self.order.items():
                print(f"{food}: {quantity}")
        else:
            print("Your order is empty.")

    def calculate_bill(self):
        total_bill = sum(self.food_menu[food] * quantity for food, quantity in self.order.items())
        print(f"Your total bill is {total_bill}.")

    def payment_mode(self, mode):
        if mode.lower() == 'cash' or mode.lower() == 'upi':
            print(f"Payment mode selected: {mode}. Thank you for your order!")
        else:
            print("Invalid payment mode. Please select either 'cash' or 'upi'.")


bot = CitCanteenBot()

print("Welcome to CIT Canteen Bot!")
print("How can I assist you today?")
while True:
    user_input = input(">> ")
    if user_input.lower() == 'display menu':
        bot.display_menu()
    elif user_input.lower() == 'view order':
        bot.view_order()
    elif user_input.lower() == 'calculate bill':
        bot.calculate_bill()
    elif user_input.lower().startswith('add'):
        _, food, quantity = user_input.lower().split()
        bot.add_to_order(food.capitalize(), int(quantity))
    elif user_input.lower().startswith('remove'):
        _, food, quantity = user_input.lower().split()
        bot.remove_from_order(food.capitalize(), int(quantity))
    elif user_input.lower().startswith('modify'):
        _, food, quantity = user_input.lower().split()
        bot.modify_order(food.capitalize(), int(quantity))
    elif user_input.lower().startswith('payment mode'):
        mode = user_input.split(' ', 2)[-1]
        bot.payment_mode(mode)
        break
    else:
        print("I'm sorry, I didn't understand that. Please try again.")
