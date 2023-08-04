def lb_to_kg(lb):
    return (lb / 0.4535924)
def kg_to_lb(kg):
    return (kg * 0.4535924)

def main():
    while True:
        print()
        print("1. Convert Pounds (lb) to Kilograms (kg)")
        print("2. Convert Kilograms (kg) to Pounds (lb)")
        print("3. Quit")

        choice = input("What would you like to do? (Press 1, 2, or 3): ")

        if choice == '1':
            lb = float(input("Enter the weight in lb: "))
            kg = lb_to_kg(lb)
            print(f"{lb:.2f} Weight is equal to {kg:.2f} Kilograms.")
        elif choice == '2':
            kg = float(input("Enter the weight in kg: "))
            lb = kg_to_lb(kg)
            print(f"{kg:.2f} Weight is equal to {lb:.2f} Pounds.")
        elif choice == '3':
            print('Goodbye!')
            break
        else:
            print("Invalid choice. Please select a valid option")


if __name__ == "__main__":
    main()