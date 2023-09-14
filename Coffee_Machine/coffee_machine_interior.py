def run_coffee_machine(menu, resources):
    coffees = ["espresso", "latte", "cappuccino"]
    profit = 0
    while True:
        starting_prompt = input("What would you like to order (espresso/latte/cappuccino)?")

        if starting_prompt.lower() == "off":
            break

        if starting_prompt.lower() == "report":
            for resource in resources:
                print(f"{resource}: {resources[resource]}.")
            print(f"money: ${profit}")

        for coffee in coffees:
            if starting_prompt.lower() == coffee:
                if not is_resources_sufficient(resources, menu[coffee]["ingredients"]):
                    break
                else:
                    if is_amount_sufficient(calculate_amount(), menu[coffee]["cost"]):
                        profit += menu[coffee]["cost"]
                        print(f"Enjoy your {coffee}")
                    break


def is_resources_sufficient(machine_resource, coffee_resource):
    for resource in coffee_resource:
        if machine_resource[resource] < coffee_resource[resource]:
            print(f"Sorry there is not enough {resource}")
            return False
        else:
            machine_resource[resource] -= coffee_resource[resource]
            return True


def is_amount_sufficient(total, cost):
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(total - cost, ndigits=2)
        print(f"Here is ${change} in change.")
        return True


def calculate_amount():
    print("Please insert your coins.")
    total = int(input("How many quarters?"))*0.25
    total += int(input("How many dimes?"))*0.1
    total += int(input("How many nickels?"))*0.05
    total += int(input("How many pennies?"))*0.01
    return total
