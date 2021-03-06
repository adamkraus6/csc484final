import mysql.connector
from datetime import date

def displayMenu():
    ans = -1
    while(True):
        print("\nWarehouse Database")
        print("\t[1]  List all customers") #
        print("\t[2]  Create a new customer") #
        print("\t[3]  List all employees") #
        print("\t[4]  List all products") #
        print("\t[5]  List all available products") #
        print("\t[6]  List all orders") #
        print("\t[7]  List all incomplete orders") #
        print("\t[8]  Mark an order as completed") #
        print("\t[9]  List all orders from a customer") #
        print("\t[10] List all orders fullfilled by an employee") #
        print("\t[11] List all products in an order") #
        print("\t[12] List all injury reports") #
        print("\t[13] Delete an injury report") #
        print("\t[14] Exit")
        ans = int(input("Enter 1 - 14: "))

        if ans < 1 or ans > 14:
            print("Incorrect input. Please enter 1 - 14\n")
        else:
            break

    return ans

def main():
    usr = input("Enter SQL username: ")
    pwd = input("Enter SQL password: ")
    mydbConn = mysql.connector.connect(
        host="localhost",
        user=usr,
        password=pwd,
        database="warehouse"
    )

    while True:
        userChoice = displayMenu()
        if userChoice == 14:
            break
        
        mycursor = mydbConn.cursor()

        if userChoice == 1:
            print("---List all customers---")
            qry = "select * from customers"
            mycursor.execute(qry)
            result = mycursor.fetchall()

            print("{:5}\t{:15}\t{:15}\t{:20}\t{:10}\t{:50}".format("ID", "First Name", "Last Name", "Position", "Phone #", "Address"))
            for row in result:
                print("{:<5}\t{:15}\t{:15}\t{:20}\t{:10}\t{:50}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        elif userChoice == 2:
            print("---Create a new customer---")
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            email = input("Enter email: ")
            phoneNum = input("Enter phone number (No dashes): ")
            address = input("Enter address: ")
            qry = "insert into customers values(NULL, \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(firstName, lastName, email, phoneNum, address)
            mycursor.execute(qry)
        elif userChoice == 3:
            print("---List all employees---")
            qry = "select * from employees"
            mycursor.execute(qry)
            result = mycursor.fetchall()
            arr = ["False", "True"]

            print("{:5}\t{:15}\t{:15}\t{:20}\t{:10}\t{:50}\t{:10}\t{:5}".format("ID", "First Name", "Last Name", "Position", "Phone #", "Address", "Salary", "Currently Employed"))
            for row in result:
                print("{:<5}\t{:15}\t{:15}\t{:20}\t{:10}\t{:50}\t{:<10}\t{:5}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], arr[int(row[7])]))
        elif userChoice == 4:
            print("---List all products---")
            qry = "select * from products"
            mycursor.execute(qry)
            result = mycursor.fetchall()

            print("{:5}\t{:50}\t{:10}\t{:5}".format("ID", "Name", "Price", "Number Remaining"))
            for row in result:
                print("{:5}\t{:50}\t{:<10}\t{:<5}".format(row[0], row[1], row[2], row[3]))
        elif userChoice == 5:
            print("---List all available products---")
            qry = "select * from products where productNumberRemaining > 0"
            mycursor.execute(qry)
            result = mycursor.fetchall()

            print("{:5}\t{:50}\t{:10}\t{:5}".format("ID", "Name", "Price", "Number Remaining"))
            for row in result:
                print("{:5}\t{:50}\t{:<10}\t{:<5}".format(row[0], row[1], row[2], row[3]))
        elif userChoice == 6:
            print("---List all orders---")
            qry = "select * from orders"
            mycursor.execute(qry)
            result = mycursor.fetchall()
            date_test = lambda str: str.strftime("%m/%d/%Y") if type(str) != type(None) else "N/A"

            print("{:5}\t{:25}\t{:25}\t{:<10}\t{:10}".format("ID", "Placed By (Customer ID)", "Fulfilled By (Employee ID)", "Placed On", "Fulfilled On"))
            for row in result:
                print("{:<5}\t{:<25}\t{:<25}\t{:10}\t{:10}".format(row[0], row[1], row[2], row[3].strftime("%m/%d/%Y"), date_test(row[4]), row[5]))
        elif userChoice == 7:
            print("---List all incomplete orders---")
            qry = "select * from orders where notes != \"Completed\""
            mycursor.execute(qry)
            result = mycursor.fetchall()
            date_test = lambda str: str.strftime("%m/%d/%Y") if type(str) != type(None) else "N/A"

            print("{:5}\t{:25}\t{:25}\t{:<10}\t{:10}".format("ID", "Placed By (Customer ID)", "Fulfilled By (Employee ID)", "Placed On", "Fulfilled On"))
            for row in result:
                print("{:<5}\t{:<25}\t{:<25}\t{:10}\t{:10}".format(row[0], row[1], row[2], row[3].strftime("%m/%d/%Y"), date_test(row[4]), row[5]))
        elif userChoice == 8:
            print("---Mark an order as completed---")
            id = int(input("Enter the order ID: "))
            qry = "update orders set notes=\"Completed\", fulfilledOn=\"{}\" where orderID={}".format(date.today().strftime("%Y-%m-%d"), id)
            mycursor.execute(qry)
        elif userChoice == 9:
            print("---List all orders from a customer---")
            id = int(input("Enter the customer ID: "))
            qry = "select * from orders where customerID={}".format(id)
            mycursor.execute(qry)
            result = mycursor.fetchall()
            date_test = lambda str: str.strftime("%m/%d/%Y") if type(str) != type(None) else "N/A"

            print("{:5}\t{:25}\t{:25}\t{:<10}\t{:10}".format("ID", "Placed By (Customer ID)", "Fulfilled By (Employee ID)", "Placed On", "Fulfilled On"))
            for row in result:
                print("{:<5}\t{:<25}\t{:<25}\t{:10}\t{:10}".format(row[0], row[1], row[2], row[3].strftime("%m/%d/%Y"), date_test(row[4]), row[5]))
        elif userChoice == 10:
            print("---List all orders fulfilled by an employee---")
            id = int(input("Enter the employee ID: "))
            qry = "select * from orders where employeeID={}".format(id)
            mycursor.execute(qry)
            result = mycursor.fetchall()
            date_test = lambda str: str.strftime("%m/%d/%Y") if type(str) != type(None) else "N/A"

            print("{:5}\t{:25}\t{:25}\t{:<10}\t{:10}".format("ID", "Placed By (Customer ID)", "Fulfilled By (Employee ID)", "Placed On", "Fulfilled On"))
            for row in result:
                print("{:<5}\t{:<25}\t{:<25}\t{:10}\t{:10}".format(row[0], row[1], row[2], row[3].strftime("%m/%d/%Y"), date_test(row[4]), row[5]))
        elif userChoice == 11:
            print("---List all products in an order---")
            id = int(input("Enter the order ID: "))
            qry = "select p.productName, numberOrdered, numberFulfilled from orderItems oi, products p where orderID={} and oi.productID = p.productID;".format(id)
            mycursor.execute(qry)
            result = mycursor.fetchall()

            print("{:50}\t{:20}\t{:20}".format("Product Name", "Number Ordered", "Number Fulfilled"))
            for row in result:
                print("{:50}\t{:<20}\t{:<20}".format(row[0], row[1], row[2]))
        elif userChoice == 12:
            print("---List all injury reports---")
            qry = "select * from injuryReports"
            mycursor.execute(qry)
            result = mycursor.fetchall()

            print("{:5}\t{:30}\t{:10}\t{:5}".format("ID", "Person Injured (Employee ID)", "Injury Date", "Description"))
            for row in result:
                print("{:<5}\t{:<30}\t{:<10}\t{:5}".format(row[0], row[1], row[2].strftime("%m/%d/%Y"), row[3]))
        elif userChoice == 13:
            print("---Delete an injury report---")
            id = int(input("Enter the injury report ID: "))
            qry = "delete from injuryReports where injuryID={}".format(id)
            mycursor.execute(qry)

if __name__ == "__main__":
    main()