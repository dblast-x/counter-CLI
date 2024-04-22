# Define a class to represent a cafeteria item
class CafeteriaItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.sold = 0  # Track the number of items sold

    def sell(self):
        self.sold += 1

    def get_total_sales(self):
        return self.sold * self.price

    def __str__(self):
        return f"{self.name} (${self.price:.2f}): {self.sold} sold"


# Create a list to store cafeteria items
def add_new_item(CafeteriaItem) -> list:
    items = []
    items.append(CafeteriaItem("Coffee", 1.50))

    return items


# Add some sample items
# items.append(CafeteriaItem("Sandwich", 5.00))
# items.append(CafeteriaItem("Salad", 4.25))


def main():
    # Main loop for cafeteria sales
    items = add_new_item()
    while True:
        print("\nCafeteria Menu:")
        for i, item in enumerate(items):
            print(f"{i+1}. {item}")

        # Get user input for item selection
        choice = input("\nEnter the number of the item you want to sell (q to quit): ")

        if choice.lower() == "q":
            break

        try:
            # Convert user input to integer and validate
            choice_int = int(choice) - 1
            if 0 <= choice_int < len(items):
                items[choice_int].sell()
                print(f"Sold 1 {items[choice_int].name}")
            else:
                print("Invalid choice. Please select a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")


if __name__ == "__main__":
    main()
