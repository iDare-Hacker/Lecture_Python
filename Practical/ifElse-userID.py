
lst = {"usernames_lst": ["Alice", "Bob", "Charlie", "David"],
        "password_lst": ["password1", "password2", "password3", "password4"],
        "location_lst": [None, None, None, None],
        "email_lst": [None, None, None, None],
        "ID_lst": [None, None, None, None]}

print ("Welcome to the User Management System.")
login_choice = input("Do you want to log in or create an account? (1/2): ")
if login_choice == "1":
    user_name = input("Enter your username: ")
    if user_name in lst["usernames_lst"]:
        index = lst["usernames_lst"].index(user_name)
        password = input("Enter your password: ")
        if password == lst["password_lst"][index]:
            print("Access granted.")
            print("Please enter your details.")
            lst["location_lst"][index] = input("Enter your location: ")
            lst["email_lst"][index] = input("Enter your email: ")
            lst["ID_lst"][index] = input("Enter your ID: ")
        else:
            print("Incorrect password. Access denied.")
    else:
        print("Username not found. Access denied.")
elif login_choice == "2":
    new_username = input("Enter a new username: ")
    if new_username in lst["usernames_lst"]:
        print("Username already exists. Please choose a different username.")
    else:
        new_password = input("Enter a new password: ")
        lst["usernames_lst"].append(new_username)
        lst["password_lst"].append(new_password)
        lst["location_lst"].append(None)
        lst["email_lst"].append(None)
        lst["ID_lst"].append(None)
        print("Account created successfully. You can now log in.")
else:
    print("Invalid choice. Please enter 1 to log in or 2 to create an account.")

print("Updated details:")
for i in range(len(lst["usernames_lst"])):
    print(f"Username: {lst['usernames_lst'][i]}, Location: {lst['location_lst'][i]}, Email: {lst['email_lst'][i]}, ID: {lst['ID_lst'][i]}")





"""user_name = input("Enter your username: ")


if user_name in lst["usernames_lst"]:
    index = lst["usernames_lst"].index(user_name)
    password = input("Enter your password: ")


    if password ==lst["password_lst"][index]:
        print("Access granted.")
        print("please enter you details")



        lst["location_lst"][index] = input("Enter your location: ")
        lst["email_lst"][index] = input("Enter your email: ")
        lst["ID_lst"][index] = input("Enter your ID: ")
    else:
        print("Incorrect password. Access denied.")
else:
    print("Username not found. Access denied.")


print("Updated details:")
for i in range(len(lst["usernames_lst"])):
    print(f"Username: {lst['usernames_lst'][i]}, Location: {lst['location_lst'][i]}, Email: {lst['email_lst'][i]}, ID: {lst['ID_lst'][i]}")
"""