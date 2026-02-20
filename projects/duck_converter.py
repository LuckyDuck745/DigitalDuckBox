def converter():
    print("📏 --- THE DUCKBOX CONVERTER ---")
    print("1. Celsius to Fahrenheit")
    print("2. Duck-Steps to Meters (1 Duck-Step = 0.25m)")
    print("3. Pounds to Kilograms")
    
    choice = input("\nSelect conversion (1-3): ")
    
    try:
        if choice == '1':
            c = float(input("Enter Celsius: "))
            f = (c * 9/5) + 32
            print(f"🔥 {c}°C is {f}°F")
        elif choice == '2':
            steps = float(input("Enter Duck-Steps: "))
            meters = steps * 0.25
            print(f"🦆 {steps} steps is roughly {meters} meters.")
        elif choice == '3':
            lbs = float(input("Enter Pounds (lbs): "))
            kg = lbs * 0.453592
            print(f"⚖️ {lbs} lbs is roughly {kg:.2f} kg.")
        else:
            print("Invalid choice, quack again.")
    except ValueError:
        print("Error: Please enter a number!")

if __name__ == "__main__":
    converter()
