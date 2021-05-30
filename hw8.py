while True:
    print("(1) Create account: ")
    print("(2) Load account information: ")
    print("(3) Exit the program: ")
    choice = int (input ("Please enter what would you like to do? "))
    
    if (choice == 1):
        accountname = input("Enter the account name: ")
        accountname = accountname + ".txt"
        file1 = open("C:/Users/SERCAN/Desktop/python-8/{}". format(accountname), "a") #It opens the file in the append mode. The file pointer exists at the end of the previously written file if exists any. 
        accountNumber = input("Please Enter the account number: ")                            #It creates a new file if no file exists with the same name
        date = input("Please Enter the date: ")
        description = input("Please Enter the description of the entry: ")
        creditNumber = input("Please Enter the credit: ")
        debitNumber = input("Please Enter the debit: ")
        debitBalance = input("Please Enter the debit balance: ")
        creditBalance = input("Please Enter the credit balance: ")
        
        writingFile = file1.writelines("{0:<15} {1:<16} {2:<15} {3:<20} {4:<15} {5:<15} {6:<15} {7:<15} \n". format("accountname","accountNumber","date","description","creditNumber","debitNumber","debitBalance","creditBalance"))
        a = file1.writelines("{0:<15} {1:<15} {2:<20} {3:<19} {4:<15} {5:<17} {6:<18} {7:<18} \n". format(accountname,accountNumber,date,description,creditNumber,debitNumber,debitBalance,creditBalance))
        
    elif (choice == 2):
        i = -1
        accountname = input("Enter the account name: ")
        file1 = open("C:/Users/SERCAN/Desktop/python-8/{}". format(accountname), "r") #It opens the file to read-only mode. The file pointer exists at the beginning. 
        list1 = []                                                                            #The file is by default open in this mode if no access mode is passed
        for writeLine in file1:
            a = writeLine.split("\t")
            list1.append(a)
        print("\nthe latest balance: \n" + list1[i][i])
        file1.close()

        print("(1) Withdrawal: ")
        print("(2) Deposit: ")
        selection = int(input("Enter your operation: "))

        if (selection == 1): 
            withdrawalAmount = input("Enter your amount to withdraw: ")
            list1.append(withdrawalAmount)
            print("You have withdrawed " + list1[i] + " money from your account! ")

            file2 = open("C:/Users/SERCAN/Desktop/python-8/{}". format(accountname), "a")
            writeLine = file2.writelines("\n {0:<15} {1:<15}". format("withdrawal Amount",withdrawalAmount))
            file2.close()

        elif (selection == 2): 
            depositAmount = input("Enter your amount to deposit: ")
            list1.append(depositAmount)
            print("You have put " + list1[i] + " amount to your deposit! ")

            file3 = open("C:/Users/SERCAN/Desktop/python-8/{}". format(accountname), "a")
            writeLine = file3.writelines("\n {0:<15} {1:<15}". format("deposit Amount",depositAmount))
            file3.close()

    else:
        break