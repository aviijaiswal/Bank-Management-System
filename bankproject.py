# Bank Management System in Python

# Dictionary to store account information
accounts = {}

# Function to create a new account
def create_account():
    name = input("Enter your name: ")
    account_number = input("Enter a unique account number: ")
    if account_number in accounts:
        print("Account number already exists. Try again.")
        return
    initial_deposit = float(input("Enter initial deposit amount: "))
    accounts[account_number] = {"Name": name, "Balance": initial_deposit}
    print(f"Account created successfully for {name} with balance {initial_deposit}")

# Function to deposit money
def deposit_money():
    account_number = input("Enter your account number: ")
    if account_number not in accounts:
        print("Account not found.")
        return
    amount = float(input("Enter amount to deposit: "))
    accounts[account_number]["Balance"] += amount
    print(f"Deposit successful. Updated balance: {accounts[account_number]['Balance']}")

# Function to withdraw money
def withdraw_money():
    account_number = input("Enter your account number: ")
    if account_number not in accounts:
        print("Account not found.")
        return
    amount = float(input("Enter amount to withdraw: "))
    if amount > accounts[account_number]["Balance"]:
        print("Insufficient balance.")
        return
    accounts[account_number]["Balance"] -= amount
    print(f"Withdrawal successful. Updated balance: {accounts[account_number]['Balance']}")

# Function to check account details
def check_account():
    account_number = input("Enter your account number: ")
    if account_number not in accounts:
        print("Account not found.")
        return
    print(f"Account Details:\nName: {accounts[account_number]['Name']}\nBalance: {accounts[account_number]['Balance']}")

# Function to close an account
def close_account():
    account_number = input("Enter your account number: ")
    if account_number not in accounts:
        print("Account not found.")
        return
    del accounts[account_number]
    print(f"Account {account_number} closed successfully.")

# Main menu function
def main_menu():
    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Account Details")
        print("5. Close Account")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            check_account()
        elif choice == '5':
            close_account()
        elif choice == '6':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
