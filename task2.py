# Temperature Converter (Celsius <-> Fahrenheit)

def celsius_to_fahrenheit(c):
    return (9/5) * c + 32

def fahrenheit_to_celsius(f):
    return (5/9) * (f - 32)

def main():
    print("=== Temperature Converter ===")
    
    try:
        temp = float(input("Enter temperature value: "))
        choice = input("Convert to (C/F): ").strip().upper()
        
        if choice == 'F':
            result = celsius_to_fahrenheit(temp)
            print(f"\n{temp}°C = {result:.2f}°F")
        
        elif choice == 'C':
            result = fahrenheit_to_celsius(temp)
            print(f"\n{temp}°F = {result:.2f}°C")
        
        else:
            print("❌ Invalid choice! Please enter C or F.")
    
    except ValueError:
        print("❌ Please enter a valid number!")

# 🔥 THIS PART WAS MISSING (VERY IMPORTANT)
if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")