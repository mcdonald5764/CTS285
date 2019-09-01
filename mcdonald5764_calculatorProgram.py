# Calculator program
# 8/25/19
# Darin McDonald
#

def main():
    loop = True;
    while loop == True:
        print("\nWelcome to the calculator program.");
        print("1. Add \n2. Subtract \n3. Divide \n4. Multiply \n5. Exit");
        choice = input("Enter a number: ");
        if choice == '1':
            addFunc();
        elif choice == '2':
            subFunc();
        elif choice == '3':
            divFunc();
        elif choice == '4':
            mulFunc();
        elif choice == '5':
            print("Goodbye");
            loop = False;
        else:
            print("Enter a valid option!")

def addFunc():
    loop = True;
    print("\nAdd");
    num1 = int(input("Enter a number: "));
    num2 = int(input("Enter a number: "));
    numMath = num1 + num2;

    print(num1," + ",num2," = ",numMath)

    while loop == True:
        print("\n1. Repeat \n2. Main Menu");
        choice = input("Enter a number: ");
        if choice == '1':
            loop = True;
            print("\nAdd");
            num1 = int(input("Enter a number: "));
            num2 = int(input("Enter a number: "));
            numMath = num1 + num2;

            print(num1," + ",num2," = ",numMath)
            
        elif choice == '2':
            loop = False;
        else:
            print("Enter a valid option!")

def subFunc():
    loop = True;
    print("\nSubtract");
    num1 = int(input("Enter a number: "));
    num2 = int(input("Enter a number: "));
    numMath = num1 - num2;

    print(num1," - ",num2," = ",numMath)

    while loop == True:
        print("\n1. Repeat \n2. Main Menu");
        choice = input("Enter a number: ");
        if choice == '1':
            loop = True;
            print("\nSubtract");
            num1 = int(input("Enter a number: "));
            num2 = int(input("Enter a number: "));
            numMath = num1 - num2;

            print(num1," - ",num2," = ",numMath)
            
        elif choice == '2':
            loop = False;
        else:
            print("Enter a valid option!")
            
def mulFunc():
    loop = True;
    print("\nMultiply");
    num1 = int(input("Enter a number: "));
    num2 = int(input("Enter a number: "));
    numMath = num1 * num2;

    print(num1," x ",num2," = ",numMath)

    while loop == True:
        print("\n1. Repeat \n2. Main Menu");
        choice = input("Enter a number: ");
        if choice == '1':
            loop = True;
            print("\nMultiply");
            num1 = int(input("Enter a number: "));
            num2 = int(input("Enter a number: "));
            numMath = num1 * num2;

            print(num1," x ",num2," = ",numMath)
            
        elif choice == '2':
            loop = False;
        else:
            print("Enter a valid option!")

def divFunc():
    loop = True;
    print("\nDivide");
    num1 = int(input("Enter a number: "));
    num2 = int(input("Enter a number: "));
    numMath = num1 / num2;

    print(num1," / ",num2," = ",numMath)

    while loop == True:
        print("\n1. Repeat \n2. Main Menu");
        choice = input("Enter a number: ");
        if choice == '1':
            loop = True;
            print("\nDivide");
            num1 = int(input("Enter a number: "));
            num2 = int(input("Enter a number: "));
            numMath = num1 / num2;

            print(num1," / ",num2," = ",numMath)
            
        elif choice == '2':
            loop = False;
        else:
            print("Enter a valid option!")


main()
