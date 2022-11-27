import subprocess as sp
import pymysql
import pymysql.cursors


def option2():
    """
    Function to implement option 1
    """
    print("Not implemented")


def option3():
    """
    Function to implement option 2
    """
    print("Not implemented")


def option4():
    """
    Function to implement option 3
    """
    print("Not implemented")


def EnterStudent():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Student Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes student details as input
        # row = {}
        print("Enter student: ")
        name = (input("Name (Fname Minit Lname - Enter NULL if no Minit exists): ")).split(' ')
        First_Name = name[0]
        # print(First_Name)
        Middle_Name = name[1]
        # print(Middle_Name)
        Last_Name = name[2]
        # print(Last_Name)
        while(1):
            Roll_Number = input("Roll Number: ")
            if len(Roll_Number)!=10:
                print("Error! Enter 10 digit IIITH roll number only.")
                continue
            else:
                break
        # print(Roll_Number)
        DOB = input("Birth Date (YYYY-MM-DD): ")
        # print(DOB)

        query = ("INSERT INTO STUDENTS VALUES('"+First_Name
        + "','"+Middle_Name+ "','"+ Last_Name+ "','"
        + Roll_Number+ "','"+ DOB+ "')")

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
    
def EnterCoordinator():
    try:
        # Takes student details as input
        # row = {}
        print("Select Coordinator From students: ")

        Roll_Number = str(input("Roll Number: "))
        # print(Roll_Number)

        query = ("INSERT INTO COORDINATOR  (COORD_Roll_Number) VALUES (" +Roll_Number+ ")" )

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterEvent():
    try:
        
        print("Enter Event: ")
        
        Event_Name = input("Name :")
                
        while(1):
            EVENT_TYPE = input("Enter event type :")
            if len(EVENT_TYPE) != "cultural" and len(EVENT_TYPE) != "technical" and len(EVENT_TYPE) == "misc":
                print("Error! Enter event type as cultural , technical and misc")
                continue
            else:
                break
        
        VENUE = input("Venue :")
        
        ORGANISED_BY = input("ORGANISED_BY :")
        
        SPONSOR = input("SPONSOR :")
        
        COORDINATOR_ID = input("COORDINATOR_ID :")
        
        APPROVED = input("APPROVED :")
        
        query = ("INSERT INTO EVENTS (Event_Name,EVENT_TYPE,VENUE,ORGANISED_BY,SPONSOR,COORDINATOR_ID,APPROVED) VALUES('"
                +Event_Name+"','"+EVENT_TYPE+"','"+VENUE+"','"+ORGANISED_BY+"','"
                +SPONSOR+"','"+COORDINATOR_ID+"','"+APPROVED+"')")


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterExpenditure():
    try:
        
        print("Enter Expenditure: ")
        
        Event_Number = input ("Event_Number : ")
        FUND_PROPOSED = input ("FUND_PROPOSED : ")
        FUND_RELEASED = input ("FUND_RELEASED : ")
            
        query = ("INSERT INTO EXPENDITURE VALUES("
                +Event_Number+","+FUND_PROPOSED+","+FUND_RELEASED+")")


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterIncome():
    try:
        
        print("Enter Income: ")
        
        SOURCE_NAME = input("SOURCE_NAME :")
        AMOUNT = input("AMOUNT :")
        
  
        query = ("INSERT INTO INCOME VALUES('"
                +SOURCE_NAME+"',"+AMOUNT+")")


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterSponsors():
    try:
        
        print("Enter Sponsors: ")
        
        SPONSOR_NAME = input("SPONSOR_NAME :")
        AMOUNT = input("AMOUNT :")
        
  
        query = ("INSERT INTO SPONSORS VALUES('"
                +SPONSOR_NAME+"',"+AMOUNT+")")


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterFoodStall():
    try:
        
        print("Enter FoodStalls: ")
        
        STALL_NAME = input("STALL_NAME :")
        AMOUNT = input("AMOUNT :")
        
  
        query = ("INSERT INTO FOOD_STALLS VALUES('"
                +STALL_NAME+"',"+AMOUNT+")")


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterFoodOps():
    try:
        
        print("Enter Food Options: ")
        
        STALL_NAME = input("STALL_NAME :")
        ITEM = input("ITEM :")
        PRICE = input("PRICE :")
        
  
        query = ("INSERT INTO FOOD_OPTIONS VALUES('"
                + STALL_NAME + "','" + ITEM + "'," + PRICE + ")")


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterEVENT_MANAGERS():
    try:
        
        print("Enter Food Options: ")
        
        Event_Number = input("Event_Number :")
        COORDINATOR_ID = input("COORDINATOR_ID :")

  
        query = ("INSERT INTO EVENT_MANAGERS VALUES('"
                + Event_Number + "'," + COORDINATOR_ID + ")")


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterPARTICIPANT_LIST():
    try:
        
        print("Enter Food Options: ")
        

        Event_Number = input("Event_Number :")
        Roll_Number = input("Roll_Number :")

  
        query = ("INSERT INTO PARTICIPANT_LIST VALUES('"
                + Event_Number + "'," + Roll_Number + ")")


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterSPONSORED_EVENTS():
    try:
        
        print("Enter Food Options: ")
        

        Event_Number = input("Event_Number :")
        SPONSOR_NAME = input("SPONSOR_NAME :")
        
        query = ("INSERT INTO SPONSORED_EVENTS VALUES('"
                + Event_Number + "'," + SPONSOR_NAME + ")")


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def BalSheet():
    #Profit-Loss
    try:
        cur.execute("SELECT SUM(AMOUNT) FROM INCOME")
        result = cur.fetchall()
        cur.execute("SELECT SUM(FUND_RELEASED) FROM EXPENDITURE")
        result1=cur.fetchall()
        Bal=float(result[0])-float(result1[0])
        print("Income: ",float(result[0]),"\tExpenditure: ",float(result1[0]))
        print("Balance: ",Bal)
    except Exception as e:
        con.rollback()
        print("Failed to read from database")
        print(">>>>>>>>>>>>>", e)

    return

def StudDetails():
    try:
        print("Check student details available for given first name")
        name=input("Enter first name to be queried: ")
        query=("S")
    except Exception as e:
        con.rollback()
        print("Failed to read from database")
        print(">>>>>>>>>>>>>", e)

    return


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        EnterStudent()
    elif(ch == 2):
        EnterCoordinator()
    elif(ch == 3):
        EnterEvent()
    elif(ch == 4):
        EnterExpenditure()
    elif(ch == 5):
        EnterIncome()
    elif(ch == 6):
        EnterSponsors()
    elif(ch == 7):
        EnterFoodStall()
    elif(ch == 8):
        EnterFoodOps()
    elif(ch == 9):
        EnterEVENT_MANAGERS()
    elif(ch == 10):
        EnterPARTICIPANT_LIST()
    elif(ch == 11):
        EnterSPONSORED_EVENTS()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    #tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host="localhost",
                              #port=30306,
                              user="root",
                              password="RKaul123",
                              db="FELICITY",
                              cursorclass=pymysql.cursors.DictCursor)
#        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
 #               tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Option 1")  # Enter student
                print("2. Option 2")  # Fire an Employee
                print("3. Option 3")  # Promote Employee
                print("4. Option 4")  # Employee Statistics
                print("5. Logout")
                ch = int(input("Enter choice> "))
  #              tmp = sp.call('clear', shell=True)
                if ch == 5:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
    #    tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
