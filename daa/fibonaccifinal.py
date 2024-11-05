# Recursive Fibonacci Function
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Non-Recursive (Iterative) Fibonacci Function
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    n1, n2 = 0, 1
    for _ in range(2, n + 1):
        n3 = n1 + n2
        n1, n2 = n2, n3
    return n2

# Main Program with User Input
def main():
    while True:  # Loop to allow repeated execution
        n = int(input("Enter the position of Fibonacci number: "))
        print("Choose the approach to calculate the Fibonacci number:")
        print("1. Recursive")
        print("2. Non-Recursive (Iterative)")
        
        choice = int(input("Enter your choice (1 or 2): "))

        if choice == 1:
            # Recursive approach
            print(f"Fibonacci sequence (Recursive):")
            for i in range(n):
                print(fibonacci_recursive(i), end=" ")
            print()  # New line after output
        elif choice == 2:
            # Non-Recursive (Iterative) approach
            print(f"Fibonacci sequence (Iterative):")
            n1, n2 = 0, 1
            print(n1, n2, end=" ")  # printing the first two numbers
            for i in range(2, n):
                n3 = n1 + n2
                print(n3, end=" ")
                n1, n2 = n2, n3
            print()  # New line after output
        else:
            print("Invalid choice. Please enter 1 for Recursive or 2 for Non-Recursive.")

        # Ask user if they want to continue
        continue_choice = input("Do you want to calculate another Fibonacci sequence? (y/n): ").strip().lower()
        if continue_choice != 'y':
            break  # Exit the loop if user does not want to continue

# Run the main function
if __name__ == "__main__":
    main()

