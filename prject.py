# Bank Management System in Python

#Dictionary to store account information

accounts = {}

# Function to create a new account
def create_account():
    name = input("Enetr your name: ")
    account_number = ("Enter Your Acount Number: ")
    if account_number in accounts:
        print ("Account number already Exist. Try again")
        return
    intial_deposit = float(input("Enter intial deposit amount: "))
    accounts[account_number] = {"Name": name, "Balance": intial_deposit}
    print(f"Account created successfully for {name} with balance {intial_deposit}")
    
# Function to deposit money
def deposit_money():
    account_number = input ("Enter your account number: ")
    if account_number not in accounts:
        print("Account not found.")
        return
    amount = float(input("Enter amount to deposit: "))
    accounts[account_number]["Balance"] += amount  
    print(f"Deposit Successful. Updated Balance: {accounts[account_number]['Balance']}")
    
# Function to withdraw money
def withdraw_money():
    account_number = print("Enetr your Account number")
    if account_number not in accounts:
        print("Account not found")
        return
    amount = float(input("Enter amount to withdraw: "))
    if amount > accounts[account_number]["Balance"]:
        print("insufficient Balance")
        return
    accounts[account_number]["Balance"] -= amount
    print(f"Withdrawal succesfully. Updated balance: {accounts[account_number]['Balance']}")
    
# Function to check account details
def check_accounts():
    account_number = input("Enter your account number: ")
    if account_number not in accounts:
        print("Account not found")
        return
    print(f"Account Details:\nName: {accounts[account_number]['Name']}\nBalance: {accounts[account_number]['Balance']}")
    
# Function to close an account
def close_account():
    account_number = input("Enetr your account number: ")
    if account_number not in accounts:
        print("Account not found")
        return
    del accounts[account_number]
    print("Account {account_number} closed succesfully")
    
#Main menu function
def main_menu():
    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Accounts Details")
        print("5. Close Account")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice =='1':
            create_account()
        elif choice == '2':
            deposit_money()
        elif choice =='3':
            withdraw_money()
        elif choice=='4':
            check_accounts()
        elif choice == '5':
            close_account()
        elif choice == '6':
            print('Exiting the system. Thank You!')
            break
        else:
            print("Invalid choice. Please try again")
            
# Run the Program
if __name__  == "__main_":
     main_menu()        