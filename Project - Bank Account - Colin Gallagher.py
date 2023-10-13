def main():

    import os, random
    from datetime import date

    accountInfoNumber = float()    # = Account Number
    accountInfoType = str()                     # = Account Type = checking, or savings

    import Project_Data_Colin_Gallagher
   
    class BankAccount(object):

        def __init__(self, accountBalanceChecking, accountBalanceSavings, accountInfoFirstName, accountInfoLastName):
            self.accountBalanceChecking = accountBalanceChecking
            self.accountBalanceSavings = accountBalanceSavings
            self.accountInfoFirstName = accountInfoFirstName
            self.accountInfoLastName = accountInfoLastName   
            self.accountInfoType = accountInfoType
            self.accountInfoNumber = accountInfoNumber     

        def headerTop(self):
            os.system('cls')
            print("----------- RoboBank ------------")
            print(" ")


        def headerWelcome(self):
            BankAccount.headerTop(self)
            print(" ")
            print("Welcome to the Robogarden Bank.")
            print(" ")


        def createAccount(self):
            os.system('cls')                                                                # Clear the screen
            BankAccount.headerTop(self)                                                     # Display the header graphic
            print("Account Creation")
            print(" ")
            self.accountInfoFirstName == input("Please enter your first name: ")
            self.accountInfoLastName == input("Please enter your last name: ")
            self.accountInfoNumber = str(date.today()) + str(random.getrandbits(4))

            print(" ")
            print("Which type of account would you like to create?")
            print(" ")
            print("C - Checking")
            print("S - Savings")
            print(" ")

            optionChoiceCA = input("Choice: ")

            if optionChoiceCA == 'C':
                self.accountInfoType = 'Checking'
            elif optionChoiceCA == 'S':
                self.accountInfoType = 'Savings'
            else:
                print("You have entered an incorrect value.")
                tryAgain = input("Try again (Y or N)?")
                print(" ")
                if tryAgain == 'Y':
                    BankAccount.createAccount(self)
                elif tryAgain == 'N':
                    exit()

            print("You have successfully created your", self.accountInfoType, "account.")

            BankAccount.optionMainMenu(self)
            

        def checkAccountBalance(self):
            os.system('cls')                                                            # Clear the screen
            BankAccount.headerTop(self)                                                    # Display the header graphic
            print("Account Balance")
            print(" ")
            print("Which account? ")
            print(" ")
            print("C - Checking")
            print("S - Savings")
            print(" ")

            optionBal = input("Choice: ")
            
            if optionBal == 'C':
                from Project_Data_Colin_Gallagher import balanceChecking
                print("The balance of your Checking account is: $", balanceChecking[-1])
            elif optionBal == 'S':
                from Project_Data_Colin_Gallagher import balanceSavings
                print("The balance of your Checking account is: $", balanceSavings[-1])
            else:
                print("You have entered an incorrect value.")
                tryAgain = input("Try again (Y or N)?")
                print(" ")
                if tryAgain == 'Y':
                    BankAccount.checkAccountBalance()
                elif tryAgain == 'N':
                    BankAccount.optionMainMenu(self) 

            BankAccount.optionMainMenu(self)                                               # Display option to return to Main Menu
        

        def getAccountInfo(self):
            os.system('cls')                                                               # Clear the screen
            BankAccount.headerTop(self)                                                    # Display the header graphic
            print("Account Creation")
            print(" ")
            print("A - Account Type")
            print("N - Account Number")
            print("H - Account Holder Name")
            print("I - Account Number")
            print(" ")

            optionChoiceAI = input("Choice: ")

            if optionChoiceAI == 'A':
                print("Your account type is:", self.accountInfoType)
            elif optionChoiceAI == 'N':
                print("Your account numer is:", self.accountInfoNumber)
            elif optionChoiceAI == 'H':
                print("This account is registered to:", self.accountInfoFirstName + " ", self.accountInfoLastName)
            elif optionChoiceAI == 'I':
                print("The account number for your account is: " + self.accountInfoNumber)

            BankAccount.optionMainMenu(self)                                               # Display option to return to Main Menu
        

        def withdrawMoney(self):
            os.system('cls')                                                            # Clear the screen
            BankAccount.headerTop(self)                                                    # Display the header graphic
            print("Which Account would you like to withdraw from?")
            print(" ")
            print("C - Checking")
            print("S - Savings")
            print(" ")

            optionChoiceW = input("Choice: ")
            dAndT = str(date.today()) + "-Withdrawl"

            if optionChoiceW == 'C':
                print("Your current balance for your Checking account is: $ ", self.accountBalanceChecking)
                print(" ")
            if optionChoiceW == 'S':
                print("Your current balance for your Savings account is: $ ", self.accountBalanceSavings)
                print(" ")
            
            withdraw = int(input("How much would you like to withdraw? $"))
            withdrawRounded = "%.2f" % float(withdraw)                                  # Rounding of user input (for user display purposes only)

            if optionChoiceW == 'C':
                if withdraw > self.accountBalanceChecking:
                    print("There are not enough funds in your account.")
                    print(" ")
                    tryAgain = input("Try again (Y or N)?")
                    print(" ")
                    if tryAgain == 'Y':
                        BankAccount.withdrawMoney(self)
                    elif tryAgain == 'N':
                        BankAccount.welcomeChoices(self)
                else:
                    Project_Data_Colin_Gallagher.checkingChangeAmount(withdraw)
                    self.accountBalanceChecking-=withdraw
                    abc=self.accountBalanceChecking
                    Project_Data_Colin_Gallagher.accountBalanceChecking(abc)
                    Project_Data_Colin_Gallagher.transactionHistoryChecking(dAndT)
                    print("Amount withdrawn: $", withdrawRounded)
                    print("New account balance for your Checking account is: $", self.accountBalanceChecking)
            elif optionChoiceW == 'S':
                if withdraw > self.accountBalanceSavings:
                    print("There are not enough funds in your account.")
                    print(" ")
                    tryAgain = input("Try again (Y or N)?")
                    print(" ")
                    if tryAgain == 'Y':
                        BankAccount.withdrawMoney(self)
                    elif tryAgain == 'N':
                        BankAccount.welcomeChoices(self)
                else:
                    Project_Data_Colin_Gallagher.savingsChangeAmount(withdraw)
                    self.accountBalanceSavings-=withdraw
                    abc=self.accountBalanceSavings
                    Project_Data_Colin_Gallagher.accountBalanceSavings(abc)
                    Project_Data_Colin_Gallagher.transactionHistorySavings(dAndT)
                    self.accountBalanceSavings=self.accountBalanceSavings-withdraw
                    print("Amount withdrawn: $", withdrawRounded)
                    print("New account balance for your Savings account is: $", self.accountBalanceSavings)

            BankAccount.optionMainMenu(self)                                               # Display option to return to Main Menu


        def depositMoney(self):                                                         # Function for depositing money into one of the two accounts
            os.system('cls')                                                            # Clear the screen
            BankAccount.headerTop(self)                                                    # Display the header graphic
            print("Which Account would you like to deposit into?")
            print(" ")
            print("C - Checking")
            print("S - Savings")
            print(" ")
            
            optionChoiceD = input("Choice: ")
            dAndT = str(date.today()) + "-Deposit"

            if optionChoiceD == 'C':
                print("Your current balance for your Checking account is: $ ", self.accountBalanceChecking)
                print(" ")
            elif optionChoiceD == 'S':
                print("Your current balance for your Savings account is: $ ", self.accountBalanceSavings)
                print(" ")
            
            deposit = float(input("How much would you like to deposit? $ "))
            depositRounded = "%.2f" % float(deposit)                                    # Rounding of user input (for user display purposes only)

            if optionChoiceD == 'C':
                Project_Data_Colin_Gallagher.checkingChangeAmount(deposit)
                self.accountBalanceChecking += deposit
                abc=self.accountBalanceChecking
                Project_Data_Colin_Gallagher.accountBalanceChecking(abc)
                Project_Data_Colin_Gallagher.transactionHistoryChecking(dAndT)
                print("Amount deposited: $", depositRounded)
                print("New account balance for your Checking account is: $", self.accountBalanceChecking)
            elif optionChoiceD == 'S':
                Project_Data_Colin_Gallagher.savingsChangeAmount(deposit)
                self.accountBalanceSavings += deposit
                abc=self.accountBalanceSavings
                Project_Data_Colin_Gallagher.accountBalanceSavings(abc)
                Project_Data_Colin_Gallagher.transactionHistorySavings(dAndT)
                # add record to transactionHistorySavings using dateAndTime:"Withdraw: ", withdraw
                print("Amount deposited: $", depositRounded)
                print("Your new account balance for your Savings account is: $", self.accountBalanceSavings)

            BankAccount.optionMainMenu(self)                                               # Display option to return to Main Menu
        

        def transactionHistory(self):                                                   # Function for displaying the Transaction History
            os.system('cls')                                                            # Clear the screen
            BankAccount.headerTop(self)                                                    # Display the header graphic
            print("Transaction History")
            print(" ")
            print("Which account? ")
            print(" ")
            print("C - Checking")
            print("S - Savings")
            print(" ")

            tranHis = input("Choice: ")
            
            if tranHis == 'C':
                from Project_Data_Colin_Gallagher import trHistChe
                from Project_Data_Colin_Gallagher import chChAm
                print("Here is a list of your 3 most recent transactions from your Checking account:")
                print(trHistChe[-4:-1])
                print(chChAm[-4:-1])
                BankAccount.optionMainMenu(self)                                           # Display option to return to Main Menu
            elif tranHis == 'S':
                from Project_Data_Colin_Gallagher import trHistSav
                from Project_Data_Colin_Gallagher import svChAm
                print("Here is a list of your 3 most recent transactions from your Savings account:")
                print(trHistSav[-4:-1])
                print(svChAm[-4:-1])
                BankAccount.optionMainMenu(self)                                           # Display option to return to Main Menu
            else:
                print("You have entered an incorrect value.")                           # Option to retry entering a valid value
                tryAgain = input("Try again (Y or N)?")
                print(" ")
                if tryAgain == 'Y':
                    BankAccount.transactionHistory(self)                                   # Restart the transactionHistory function
                elif tryAgain == 'N':
                    BankAccount.optionMainMenu(self) 


        def optionMainMenu(self):                                                       # Function used to offer to go back to the Main Menu - Used at the end of each other function that displays content
            print(" ")
            print("Would you like to go to the main menu?")
            print(" ")
            print("Y - Yes")
            print("N - No")
            print(" ")

            mainMenu = input("Choice: ")

            if mainMenu == "Y":
                BankAccount.welcomeChoices(self)
            elif mainMenu == "N":
                os.system("cls")
                BankAccount.headerTop(self)
                print(" ")
                print("  Thanks for visiting RoboBank.")
                print(" ")
                print("       Have a great day!")
                print(" ")
                print(" ")
                exit()

        def welcomeChoices(self):                                                       # Function to display first and request which function the user would like to use
            os.system('cls')                                                            # Clear the screen
            BankAccount.headerTop(self)                                                    # Display the header graphic
            print("Please choose one of the following options: ")
            print(" ")
            print("1 - Create Account")
            print("2 - Account Balance")
            print("3 - Get Account Information")
            print("4 - Withdraw Money")
            print("5 - Deposit Money")
            print("6 - Transaction History")
            print(" ")
            print("7 - Quit")
            print(" ")

            optionChoice = input("Choice: ")
            ls1=['1','2','3','4','5','6','7']

            while True:                                                                 # Input validation - Make sure the user enters numbers only
                try:
                    int(optionChoice)
                    while True:                                                         # Input validation - Make sure the user enters one of the number options only
                        print(optionChoice)
                        if optionChoice in ls1:
                            if optionChoice == '1':
                                BankAccount.createAccount(self)
                            elif optionChoice == '2':
                                BankAccount.checkAccountBalance(self)
                            elif optionChoice == '3':
                                BankAccount.getAccountInfo(self)
                            elif optionChoice == '4':
                                BankAccount.withdrawMoney(self)
                            elif optionChoice == '5':
                                BankAccount.depositMoney(self)
                            elif optionChoice == '6':
                                BankAccount.transactionHistory(self)
                            elif optionChoice == '7':                                   # Exit option (it only displays text within an IDE)
                                os.system("cls")
                                BankAccount.headerTop(self)
                                print(" ")
                                print("  Thanks for visiting RoboBank.")
                                print(" ")
                                print("        Have a great day!")
                                print(" ")
                                print(" ")
                                exit()
                        else:                                                           # If the user entered a number but it wasn't one of the options, they get the choice menu again
                            #os.system('cls')
                            print(optionChoice, " is not a valid choice.")
                            print(" ")
                            print("Please choose one of the following options: ")
                            print(" ")
                            print("1 - Create Account")
                            print("2 - Account Balance")
                            print("3 - Get Account Information")
                            print("4 - Withdraw Money")
                            print("5 - Deposit Money")
                            print(" ")
                            print("6 - Quit")
                            optionChoice = input("New choice: ")
                except ValueError:
                    print("Please enter number choices only.")
                    optionChoice = input("New choice: ")

    start = BankAccount(0,0,0,0)
    start.welcomeChoices()
    

main()