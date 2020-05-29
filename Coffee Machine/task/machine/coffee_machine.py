# Starting values (of global variables)
def get_response(text):
    print("")
    print(text)
    selection = input()
    return selection


class CoffeeMachine:
    def __init__(self, w, m, b, c, dollars):
        self.water = w
        self.milk = m
        self.beans = b
        self.cups = c
        self.money = dollars

    def remaining(self):
        print("")
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print("$" + str(self.money) + " of money")

    def enough(self, w, m, b, c):
        # checks if there is enough stock for sale
        if self.water - w < 0:
            return "water"
        elif self.milk - m < 0:
            return "milk"
        elif self.beans - b < 0:
            return "beans"
        elif self.cups - c < 0:
            return "cups"
        else:
            return "ok"

    def buy(self):
        coffee_type = get_response("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
        if coffee_type == "1":
            # Espresso:
            resource = self.enough(250, 0, 16, 1)
            if resource == "ok":
                self.water -= 250
                self.milk -= 0
                self.beans -= 16
                self.cups -= 1
                self.money += 4
                print("I have enough resources, making you a coffee!")
            else:
                print("Sorry, not enough " + resource + "!")
        elif coffee_type == "2":
            # Latte:
            resource = self.enough(350, 75, 20, 1)
            if resource == "ok":
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
                print("I have enough resources, making you a coffee!")
            else:
                print("Sorry, not enough " + resource + "!")
        elif coffee_type == "3":
            # Cappuccino:
            resource = self.enough(200, 100, 12, 1)
            if resource == "ok":
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
                print("I have enough resources, making you a coffee!")
            else:
                print("Sorry, not enough " + resource + "!")

    def fill(self):
        self.water += int(get_response("Write how many ml of water do you want to add: "))
        self.milk += int(get_response("Write how many ml of milk do you want to add: "))
        self.beans += int(get_response("Write how many grams of coffee beans do you want to add: "))
        self.cups += int(get_response("Write how many disposable cups of coffee do you want to add: "))

    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0


# Main programs
command = ""
machine = CoffeeMachine(400, 540, 120, 9, 550)
while command != "exit":
    command = get_response("Write action (buy, fill, take, remaining, exit): ")
    if command == "buy":
        machine.buy()
    elif command == "fill":
        machine.fill()
    elif command == "take":
        machine.take()
    elif command == "remaining":
        machine.remaining()
