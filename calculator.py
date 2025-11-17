try:
    a=int(input("Enter 1st number:- "))
    b=int(input("Enter 2nd number:- "))
    o=input("Please enetr your operation which you want +,-,*,/")
    match o:
        case '+':
            print(a+b)
        case '-':
            print(a-b)
        case '*':
            print(a*b)
        case '/':
            print(a/b)
except:
    print("Please enter a valid number")
