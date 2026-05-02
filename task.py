# Simple Interest Calculator

def calculate_simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

def main():
    print("=== Simple Interest Calculator ===")
    
    try:
        # Taking input from user
        principal = float(input("Enter Principal amount (P): "))
        rate = float(input("Enter Rate of interest (R): "))
        time = float(input("Enter Time (T in years): "))
        
        # Calculate SI
        interest = calculate_simple_interest(principal, rate, time)
        
        # Output result
        print(f"\nSimple Interest = {interest:.2f}")
    
    except ValueError:
        print("❌ Please enter valid numeric values!")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")