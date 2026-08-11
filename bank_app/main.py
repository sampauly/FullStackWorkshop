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

    # create another curstomer
    tommy = Customer(name="Tommy", email="tommythecat@gmail.com", branch_id=citi_bank.branch_id, customer_id=2)

    citi_bank.add_customer(sam)
    citi_bank.add_customer(tommy)

    # initialize bank accounts for new customer
    checking = CheckingAccount(account_id="C01", balance=150)
    savings = SavingsAccount(account_id="S01", balance=20000)

    checking_2 = CheckingAccount(account_id="C02", balance=50)
    savings_2 = SavingsAccount(account_id="S02", balance=150)

    # add bank accounts to customer accounts
    sam.accounts.append(checking)
    sam.accounts.append(savings)

    tommy.accounts.append(checking_2)
    tommy.accounts.append(savings_2)

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
                from_id = input("Enter the account ID to transfer from: ")
                amount = float(input("Enter the amount to transfer: "))
                to_id = input("Enter the account ID to transfer to: ")
                from_acct = find_account(sam, from_id)
                if from_acct is None:
                    print("Account not found")
                    continue
                to_acct = find_account(sam, to_id)
                if to_acct is None:
                    print("Account not found")
                    continue
                citi_bank.transfer(from_acct, to_acct, amount)
                print(f"New balances:\n{from_id}:   ${from_acct.balance}\n{to_id}:    ${to_acct.balance}")
            case 5:
                print("Goodbye")
                break
            case _:
                print("Invalid command")


if __name__ == "__main__":
    main()