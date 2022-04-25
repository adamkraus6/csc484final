import mysql.connector

def displayMenu():
    ans = -1
    while(True):
        print("")
        ans = int(input("Enter 1 - 5: "))

        if ans < 1 or ans > 5:
            print("Incorrect input. Please enter 1 - 5\n")
        else:
            break

    return ans

mydbConn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="warehouse"
)

print(mydbConn)
print()

while True:
    userChoice = displayMenu()
    if userChoice == 5:
        break
    
    mycursor = mydbConn.cursor()

    # if elses

        


    