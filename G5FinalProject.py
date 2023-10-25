import datetime, os, time

class ATM:
    def __init__(account):
        account.balance = 100

    def display_balance(account):
        print(f"\033[32mYour Current Balance Is: ${account.balance}\033[0m")
        time.sleep(1)
        os.system("cls")

    def withdraw_cash(account, amount):
        global total
        if amount <= account.balance:
            account.balance -= amount
            total = amount
            print(f"\033[32mWITHDRAWN: ${total}\033[0m")
        else:
            print("\033[31mInsufficient Balance.\033[0m")
            time.sleep(1)
            os.system("cls")

    def deposit_cash(account, amount):
        account.balance += amount
        os.system("cls")

    def main_menu(account):
        while True:
            print()
            print("\n\033[32mMain Menu:")
            print("1. Check Balance")
            print("2. Withdraw Cash")
            print("3. Deposit Cash")
            print("4. Exit Lux Bank")
            print()

            choice = float(input("Select Transaction (1-4): \033[0m"))
            os.system("cls")
            if choice == 1:
                account.display_balance()

                os.system("cls")
                decide = input("\033[32mWould You Like To Exit Now?\nType 1 To e\Exit\n Type 2 To Continue.\n")
                if decide == "1":
                    time.sleep(1)
                    print("Loading....")
                    time.sleep(1)
                    os.system("cls")
                    print("Please wait for your receipt to be printed.")
                    time.sleep(1)

                    print("")
                    print("\033[32m=========== LUX BANK ===================")
                    now = datetime.datetime.now()
                    print("DATE:", now.strftime("%y-%m-%d"))
                    now = datetime.datetime.now()
                    print("TIME:", now.strftime("%H:%M:%S"))
                    print("========================================")
                    print(f"ACCOUNT NUMBER: {account_number}")
                    print(f"CUSTOMER NAME: {full}")
                    print("WITHDRAW FROM: BDO")
                    print("TRANSACTION TYPE: BALANCE INQUIRY")
                    print("========================================")
                    print(f"AMOUNT: ${0}")
                    print(f"ACCOUNT BALANCE: ${account.balance}")
                    print("========================================")
                    print("PLEASE RETAIN OR DISPOSE YOUR RECEIPT THOUGHTFULLY\033[0m")

                    print("\033[32mTHANK YOU FOR USING LUX BANK!")
                    break
                else:
                    os.system("cls")

            elif choice == 2:
                account.withdraw_menu()

                decide = input("\033[32mWould You Like To Exit Now?\nType 1 To e\Exit\n Type 2 To Continue.\n")
                if decide == "1":
                    rec = input("\033[32mWould You Like A Receipt?\n Type 1 To Print Receipt\n Type 2 To Continue.\n")
                    if rec == "1":

                        time.sleep(1)
                        print("Loading....")
                        time.sleep(1)
                        os.system("cls")
                        print("Please Wait While We Print Your Receipt...")
                        time.sleep(1)

                        print("")
                        print("\033[32m============= LUX BANK ================")
                        now = datetime.datetime.now()
                        print("DATE:", now.strftime("%y-%m-%d"))
                        now = datetime.datetime.now()
                        print("TIME:", now.strftime("%H:%M:%S"))
                        print("========================================")
                        print(f"ACCOUNT NUMBER: {account_number}")
                        print(f"CUSTOMER NAME: {full}")
                        print("WITHDRAWN FROM: LUX")
                        print("TRANSACTION TYPE: WITHDRAWAL")
                        print("========================================")
                        print(f"AMOUNT: ${total}")
                        print(f"ACCOUNT BALANCE: ${account.balance}")
                        print("========================================")
                        print("PLEASE RETAIN OR DISPOSE THIS RECEIPT THOUGHTFULLY\033[0m")

                        print("\033[32mTHANK YOU FOR USING LUX BANK!")
                    else:
                        print("")
                        print("\033[32mTHANK YOU FOR USING LUX BANK!")
                        print("")
                    break

                os.system("cls")
            elif choice == 3:

                deposit_amount = float(input("\033[32mEnter Deposit Amount: $"))
                account.deposit_cash(deposit_amount)
                print(f"\033[32mDeposited ${deposit_amount} Successfully.\033[0m")

                decide = input("\033[32mWould You Like To Exit Now?\nType 1 To e\Exit\n Type 2 To Continue.\n")
                if decide == "1":
                    rec = input("\033[32mWould You Like A Receipt?\n Type 1 To Print Receipt\n Type 2 To Continue.\n")
                    if rec == "1":

                        time.sleep(1)
                        print("Loading....")
                        time.sleep(1)
                        os.system("cls")
                        print("Please Wait While We Print Your Receipt...")
                        time.sleep(1)

                        print("")
                        print("\033[32m=========== LUX BANK ===========")
                        now = datetime.datetime.now()
                        print("DATE:", now.strftime("%y-%m-%d"))
                        now = datetime.datetime.now()
                        print("TIME:", now.strftime("%H:%M:%S"))
                        print("========================================")
                        print(f"ACCOUNT NUMBER: {account_number}")
                        print(f"CUSTOMER NAME: {full}")
                        print("DEPOSIT FROM: LUX")
                        print("TRANSACTION TYPE: DEPOSIT")
                        print(f"AMOUNT: ${deposit_amount}")
                        print("========================================")
                        print(f"ACCOUNT BALANCE: ${account.balance - deposit_amount}")
                        print(f"NEW BALANCE: ${account.balance}")
                        print("========================================")
                        print("PLEASE RETAIN OR DISPOSE THIS RECEIPT THOUGHTFULLY\033[0m")
                        print("\033[32mTHANK YOU FOR USING LUX BANK!")
                    else:
                        print("")
                        print("\033[32mTHANK YOU FOR USING LUX BANK!")
                        print("")
                    break

                os.system("cls")
            elif choice == 4:
                print("\033[32mTHANK YOU FOR USING LUX BANK!")
                break
            else:
                print("\033[31mChoice Invalid. Please Try Again.\033[0m")
                time.sleep(1)
                os.system("cls")

    def withdraw_menu(account):
        ten = 10; twenty = 20; fifty = 50; hundred = 100;
        print("\n\033[32mWithdraw Menu:")
        print("1. $10")
        print("2. $20")
        print("3. $50")
        print("4. $100")
        print("5. Enter amount")
        choice = float(input("Choose Withdraw Amount (1-5): "))
        os.system("cls")
        if choice == 1:
            account.withdraw_cash(ten)
        elif choice == 2:
            account.withdraw_cash(twenty)
        elif choice == 3:
            account.withdraw_cash(fifty)
        elif choice == 4:
            account.withdraw_cash(hundred)
        elif choice == 5:
            wd = float(input("\033[32mEnter Amount To Withdraw: "))
            os.system("cls")
            if wd > account.balance:
                print("\033[31mInsufficient Balance.\033[0m")
                time.sleep(1)
                os.system("cls")
            else:
                account.withdraw_cash(wd)
        else:
            print("\033[31mChoice Invalid. Please Try Again.\033[0m")
            time.sleep(1)
            os.system("cls")

    def date_now():
        now = datetime.datetime.now()
        print("Date:", now.strftime("%y-%m-%d"))

    def time_now():
        now = datetime.datetime.now()
        print("Time:", now.strftime("%H:%M:%S"))


#LOGIN

acc_number = {123456 : 4242}
global name, full;
hello = input("\033[32m\nWelcome To LUX Bank!\nHave An Account Already? Type 1 To Continue\nNew User? Type 2 To Register An Account\n   : ")
print()
if hello == "1":
    attempts = 0
    while attempts < 5:

        global account_number
        account_number = int(input("\033[32mACCOUNT NUMBER: "))
        password = int(input("\033[32mPIN: "))
        name = input("Enter your full name: ")
        full = name.upper()

        if account_number in acc_number and acc_number[account_number] == password:
            print(f"WELCOME {full}!")
            if __name__ == "__main__":
                atm = ATM()
                atm.main_menu()
            break
        else:
            attempts += 1
            if attempts >= 5:
                print("\033[31mNo More Attempts Left. Please Try Again Later.\033[0m")
                break
            else:
                print("\033[31mLogin Failed. Please Try Again.\033[0m")

else:
    while True:
        number = int(input("\033[32mCreate Account Number\n(Ex: 0**********)\n: "))
        pin = int(input("\033[32mCreate Pin\n(Ex: 0***)\n: "))
        fname = input("Enter Your Complete Name: ")
        print()
        attempts = 0

        if number not in acc_number:
            acc_number[number] = pin
            while attempts < 5:  # Set a maximum of 5 login attempts
                account_number = int(input("\033[32mACCOUNT NUMBER: "))
                password = int(input("\033[32mPIN: "))
                name = input("Enter Your Full Name: ")
                full = name.upper()

                if account_number in acc_number and acc_number[account_number] == password:
                    print(f"WELCOME {full}!")
                    if __name__ == "__main__":
                       atm = ATM()
                       atm.main_menu()
                    break
                else:
                    attempts += 1
                    if attempts >= 5:
                        print("\033[31mNo More Attempts Left. Please Try Again Later.\033[0m")
                        break
                    else:
                        print("\033[31mLogin Failed\nPlease Try Again.\033[0m")
            break
        else:
            print("ACCOUNT ALREADY EXISTED")
            print()