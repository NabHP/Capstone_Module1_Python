from tabulate import tabulate

# Data for login
User_ID = "NabHP"
User_password = "1234"

# Function for checking login
def check_credentialUser ():
    while True:
        input_username1 = input("Input your username: ")
        input_password1 = input("Input your password: ")
        if input_username1 == User_ID and input_password1 == User_password:
           print("Login successful!")
           break
        else:
            print("Invalid username or password.Please try again!")




#Function for Login Menu
def Login_menu(): 
    while True:
        Main_Title = '''
        ====Welcome to My Personal Library====\n'''
        print(Main_Title.upper())
        print('''What do you want to choose?
                1. Login
                2. Exit program''')
        input_mainmenu = int(input("Enter the number menu: "))
        if input_mainmenu == 1:
            print("Welcome User!")
            check_credentialUser()
            continue_session = Main_Menu()
            if continue_session == False:
                break
        elif input_mainmenu == 2:
            print("Exiting program...")
            break
        else:   
            print("Invalid input. Please try again.")
    


# Data set
Book_List = [{"title": "Right Thing, Right Now", "year": 2024, "publisher": "Abrams Books"},
             {"title": "Discipline is Destiny", "year": 2022, "publisher": "Sterling Publishing"},
             {"title": "Courage is Calling", "year": 2021, "publisher": "Chandelwick Press"},
             {"title": "Stillness is the Key", "year": 2019, "publisher": "Harper Collins"},
             {"title": "Ego is the Enemy", "year": 2016, "publisher": "Bloomsbury Publishing"}           
]


# Create and View book's table
def Display_BookList():
    Book_List_table = []
    for index,book in enumerate(Book_List):
        Book_List_table.append ([index + 1 , book["title"], book["year"], book["publisher"]])
    print(tabulate(Book_List_table, headers=["No", "Title", "Year", "Publisher"], tablefmt="fancy_grid"))



# Function for displaying the menu
def Menu ():
    print('''
    ===== Welcome to Main Menu =====\n
    1. View Books
    2. Add Book
    3. Delete Book
    4. Edit Data
    5. Sorted books
    6. Back to Login Menu
          ''')


# Function to go back to Main Menu
def return_to_Main_Menu():
    while True:
        back_to_MM = input("Do you want to return to Main Menu? (yes/no)").lower()
        if back_to_MM == "yes":
            print("Return to Main Menu.")
            return True
        elif back_to_MM == "no":
            print("That's okay.")
            return False
        else:
            print("Invalid input.")



# Function for adding a new book
def Add_newbook ():
    while True:
        input_booktitle = input("Enter the title of the book: ")
        input_bookyear = input("Enter the book year: ")
        input_bookpublisher = input("Enter the book publisher: ")
        try:
            input_bookyear = int(input_bookyear)
        except ValueError:
            print("Invalid input. Please input only number for the book year.")
            continue

        NewBook =(f'''
        Title: {input_booktitle}
        Year: {input_bookyear},
        Publisher: {input_bookpublisher}
        ''')
        print(f"You just add a new book information to the table:\n{NewBook}")
        Book_List.append({"title": input_booktitle, "year": input_bookyear, "publisher": input_bookpublisher})
        print("New book has added successfully.")
        Display_BookList()
        back_to_mm = return_to_Main_Menu()
        if back_to_mm == True:
            break
              


# Function for deleting a book
def Delete_book():
    Display_BookList()
    try:
        while True:
            index_to_delete = int(input("Enter book's number to delete: "))
            if index_to_delete < 1 or index_to_delete > len(Book_List):
                print("Invalid book number.")
                return
            else:
                Deleted_data = Book_List.pop(index_to_delete - 1)
                print("Book is deleted.")
                Display_BookList()
                back_to_mm = return_to_Main_Menu()
                if back_to_mm == True:
                    break
                else:
                    continue
                break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except IndexError:
        print("Invalid book number. Please enter a valid book number.")

                          

# Function for editing the table
def Edit_Table ():
    Display_BookList()
    while True:
        try:
            Book_Number = int(input("Enter the book number you want to edit: "))
            if 0 <= Book_Number < len(Book_List):
                field = input("Enter which field you want to edit (title/year/publisher):  "). lower()
                if field in ["title", "year", "publisher"]:
                    edit_value = input(f"Enter new value for {field}: ")
                    if field == "title":
                        edit_value = str(edit_value)
                    elif field == "year":
                        edit_value = int(edit_value)
                    elif edit_value == "publisher":
                        edit_value = str(edit_value)
                    Book_List[Book_Number-1][field] = edit_value
                    print ("Book information is edited successfully.")
                    Display_BookList()
                    back_to_mm = return_to_Main_Menu()
                    if back_to_mm == True:
                        break
                else:
                    print("Invalid input. Please enter invalid number and field.")
        except ValueError:
            print("Invalid input. Error, sorry.")



# Function to return to Login Menu
def Return_Login_menu():
    while True:
        back_to_LoginMM = input("Are you sure you want to go back to Login Menu? (yes/no)")
        if back_to_LoginMM == "yes":
            print("Return to Login Menu.")
            return True
        elif back_to_LoginMM == "no":
            print("That's okay.")
            return False
        else:
            print("Invalid input. Please try again.")



# Function for sorting books
def sorted_books_by_field():
    try:
        while True:
            field = ["title", "year", "publisher"]
            info_to_sorted = input("Enter field you want to sort(title/year/publisher): ").lower()
            if info_to_sorted in field:
                sorted_books = sorted(Book_List, key=lambda x: x[info_to_sorted])
                Book_List_sorted = []
                for index, book in enumerate(sorted_books):
                    Book_List_sorted.append([index + 1, book["title"], book["year"], book["publisher"]])
                print(tabulate(Book_List_sorted, headers=["No", "Title", "Year","Book"], tablefmt="fancy_grid"))
                back_to_mm = return_to_Main_Menu()
                if back_to_mm == True:
                    break
            elif info_to_sorted not in field:
                print("Invalid input. Please try again.")
            else:
                print("Please try to input the right keyword.")
    except KeyError:
        print("Error: One or more book information are missing in the specific fields. Please check the data and try again.")




# Main Menu
def Main_Menu ():
    while True:
        Menu ()
        input_commands_Admin = int(input("Enter the key menu: "))
        if input_commands_Admin == 1:
            Display_BookList()
        elif input_commands_Admin == 2:
            Add_newbook ()
        elif input_commands_Admin == 3:
            Delete_book() 
        elif input_commands_Admin == 4:
            Edit_Table()
        elif input_commands_Admin == 5:
            sorted_books_by_field()
        elif input_commands_Admin == 6:
            back_to_login_menu = Return_Login_menu()
            if back_to_login_menu:
                return True
            elif not back_to_login_menu:
                back_to_mm = return_to_Main_Menu()
                if back_to_mm == False:
                    break
        else:
            print("Invalid input. Please input the right key menu.")

Login_menu()











