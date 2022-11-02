while True:
    print("select an option from menu")
    print("1 add book")
    print("2 view all book")
    print("3 search a book")
    print("4 update the book")
    print("5 delete a book")
    print("6 exit")

    choice = int(input("Enter an option: "))
    if(choice==1):
        print("book enter selected")
    elif(choice==2):
        print("view book selected")
    elif(choice==3):
        print("search book selected")
    elif(choice==4):
        print("update book selected")
    elif(choice==5):
        print("delete book selected")
        
    elif(choice==6):
        break