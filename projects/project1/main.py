# Starting file for Project 1
# Be sure to include your name, date, and DEV 128 in the comments header

# Jack Bull
# 11/10/26
# DEV 128 

import sqlite3

# function to set up our database
def setup_db(conn, cursor):

    cursor.execute("DROP TABLE IF EXISTS user;")

    # create the table if it doesn't already exist
    # note that primary keys are automatically created in sqlite3 and referenced as rowid
    cursor.execute("CREATE TABLE IF NOT EXISTS user (first_name TEXT, last_name TEXT, email TEXT, phone TEXT, street_address TEXT, city TEXT, state TEXT, zip_code TEXT)")

    # create 5 records of data
    cursor.execute("INSERT INTO user VALUES (\"Tony\", \"Stark\", \"Ironman@stark.com\", \"555-111-2222\", \"12345 Main Street\", \"Malibu\", \"CA\", \"98581\")")
    cursor.execute("INSERT INTO user VALUES (\"Carol\", \"Danvers\", \"Marvel@stark.com\", \"555-123-2424\", \"1233 Michigan Ave.\", \"Boston\", \"MA\", \"00248\")")
    cursor.execute("INSERT INTO user VALUES (\"Steve\", \"Rogers\", \"Steve@marvel.com\", \"555-222-5678\", \"456 Ocean Ave.\", \"Seattle\", \"WA\", \"98001\")")
    cursor.execute("INSERT INTO user VALUES (\"Natasha\", \"Romanov\", \"natasha@marvel.com\", \"555-333-6789\", \"111 Arroyo Dr.\", \"Los Angeles\", \"CA\", \"90210\")")
    cursor.execute("INSERT INTO user VALUES (\"Wanda\", \"Maximoff\", \"Wanda@marvel.com\", \"555-333-1234\", \"253 Sunnydale Ave.\", \"Las Vegas\", \"NV\", \"89101\")")

    return cursor

# function to list the names in our database
def list_names(conn, cursor):
        # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name FROM user")

    # store the results of the query to a list called users
    users = cursor.fetchall()

    # loop through results of the querey
    for this_user in users:
        print(this_user[0], this_user[1], this_user[2])
    print()

# function to list the email and phone number of the names in our database
def list_contact_info(conn, cursor):

    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, email, phone, state FROM user")

    # store the results of the query to a list called users
    users = cursor.fetchall()

    # loop through results of the querey
    for this_user in users:
        print(this_user[0], this_user[1], this_user[2], this_user[3], this_user[4], this_user[5])
    print()


# function to list the address and names in our database.
def list_location(conn, cursor):

    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, street_address, city, state, zip_code FROM user")

    # store the results of the query to a list called users
    users = cursor.fetchall()

    # loop through results of the querey
    for this_user in users:
        print(this_user[1], this_user[2], this_user[3], this_user[4], this_user[5], this_user[6])
    print()


# function to display the menu of options
def menu():
    # Prints the menu for the 5 options the user can input
    print("* " * 21)
    print("- - - Marvel Database Program Menu - - -")
    print("* " * 21 + "\n")
    print("Please select an option from the below list:\n")
    print("0 - Initialize Database - Be careful! This will wipe all data!")
    print("1 - List all names of the Marvel characters")
    print("2 - List all names, email, and phone number for all users")
    print("3 - List all names and address for all users")
    print("4 - Add new user")
    print("5 - Exit the program\n")

# function to add a user to the database
def add_user(conn, cursor):

    print("Add New User\n")

    # get the values from the user
    input_first_name = input("First Name: ")
    input_last_name = input("Last Name: ")
    input_email = input("Email: ")
    input_phone_number = input("Phone: ")
    input_street = input("Street Address: ")
    input_city = input("City: ")
    input_state = input("2 Digit State: ")
    input_zip_code = input("Zip Code: ")

    # prepare insert statement useing ? for each item to be inserted
    sql = """
        INSERT INTO user (first_name, last_name, email, phone, street_address, city, state, zip_code)
        VALUES (?,?,?,?,?,?,?,?)
        """

    #insert the data into the database
    cursor.execute(sql, (input_first_name, input_last_name, input_email, input_phone_number, input_street,input_city, input_state, input_zip_code))
    print("\nCharacter added, thank you!\n")

    return cursor

def main():

    conn = sqlite3.connect("users.db")

    # create a cursor that we will use to move through the database
    cursor = conn.cursor()

    # loop to go thought the menu and process the user selections

    while True:
        menu()

        # gets choice value 0-5 from the user, validating if they enter an integer between 0-5
        while True:
            try:
                choice = int(input("Please select your option: "))
                print()
                if choice not in [0,1,2,3,4,5]:
                    print("Invalid input. Please enter a number, 0 through 5\n")
                    continue
                else:   
                    break
            except ValueError:
                print("Invalid input. Please enter a number, 0 through 5\n")

        # if / elif / else statements to perform an action based on the user input
        if choice == 0:
            cursor = setup_db(conn, cursor)
        elif choice == 1:
            list_names(conn,cursor)
        elif choice == 2:
            list_contact_info(conn, cursor)
        elif choice == 3:
            list_location(conn, cursor)
        elif choice == 4:
            add_user(conn, cursor)
        else:
            break

    # save the updates to the database - if you don't commit any updates/inserts to the database will not be saved
    conn.commit()

    # close the connection
    conn.close()

    # Goodbye message
    print("Thank you for using our Marvel database!")

if __name__ =="__main__":
    main()