def converter():
    print("📏 THE DUCKBOX CONVERTER")
    print("1. Celsius to Fahrenheit")
    print("2. Duck-Steps to Meters (1 Duck-Step = 0.25m)")
    
    choice = input("\nSelect conversion (1-2): ")
    
    if choice == '1':
        c = float(input("Enter Celsius: "))
        f = (c * 9/5) + 32
        print(f"🔥 {c}°C is {f}°F")
    elif choice == '2':
        steps = float(input("Enter Duck-Steps: "))
        meters = steps * 0.25
        print(f"🦆 {steps} steps is roughly {meters} meters.")
    else:
        print("Invalid choice, quack again.")

if __name__ == "__main__":
    converter()
