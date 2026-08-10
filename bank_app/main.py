from customer import Customer
from accounts import CheckingAccount, SavingsAccount
from bank import Bank

def find_account(customer, account_id):
    for acct in customer.accounts:
        if acct.account_id == account_id:
            return acct
    return None

def list_accounts(customer):
    print(f"\n{customer.name}'s accounts:")
    for acct in customer.accounts:
        print(f"{acct.account_id} ({type(acct).__name__}): ${acct.balance}")

def main():
    print("Welcome to the bank")

    # initizialize citi bank
    citi_bank = Bank(branch_id=1)

    # initialize a customer at citi bank
    sam = Customer(name="Sam", email="samuelpauly02@gmail.com", branch_id=citi_bank.branch_id, customer_id=1)

    citi_bank.add_customer(sam)

    # initialize bank accounts for new customer
    checking = CheckingAccount(account_id="C01", balance=150)
    savings = SavingsAccount(account_id="S01", balance=20000)

    # add bank accounts to customer accounts
    sam.accounts.append(checking)
    sam.accounts.append(savings)

    # output user console
    while True:
        print("\nWhat would you like to do?\n1- List accounts\n2- Deposit\n3- Withdraw\n4- Transfer money\n5- Exit\n")
        command = int(input("Enter command: "))
        match command:
            case 1:
                list_accounts(sam)
            case 2:
                acct_id = input("Enter account ID to deposit to: ")
                acct = find_account(sam, acct_id)
                if acct is None:
                    print("Account not found")
                    continue
                amount = float(input("Amount to deposit: "))
                acct.deposit(amount)
                print(f"New balance: ${acct.balance}")
            case 3: 
                acct_id = input("Enter account ID to withdraw from: ")
                acct = find_account(sam, acct_id)
                if acct is None:
                    print("Account not found")
                    continue
                amount = float(input("Amount to withdraw: "))
                try:
                    acct.withdraw(amount)
                    print(f"New balance: ${acct.balance}")
                except ValueError as e:
                    print(f"Withdrawal failed: {e}")
            case 4:
                print("Coming soon")
            case 5:
                print("Goodbye")
                break
            case _:
                print("Invalid command")

if __name__ == "__main__":
    main()