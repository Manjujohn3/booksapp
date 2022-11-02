import mysql.connector

mydb= mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'librarydb')
mycursor = mydb.cursor()

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
        name = input("enter the name")
        category = input("enter the value")
        author = input("enter the author name")
        charge = input("enter the charge")
        sql = 'INSERT INTO `books`(`name`, `category`, `author`, `charge`) VALUES (%s,%s,%s,%s)'
        data = (name,category,author,charge)
        mycursor.execute(sql , data)
        mydb.commit()
        print("value inserted succesfully") 

    elif(choice==2):
        print("view book selected")
        sql = 'SELECT * FROM `books`'
        mycursor.execute(sql)
        result =  mycursor.fetchall()
        for i in result:
            print(i) 


    elif(choice==3):
      print("search book selected")
    elif(choice==4):
      print("update book selected")
    elif(choice==5):
      print("delete book selected")
        
    elif(choice==6):
      break