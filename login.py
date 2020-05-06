import dashboard


# login function
def login_area(name, username, phone, email, password):
    print("Login Area")
    user_name_attempt = input("Enter Username: ")
    password_attempt = input("Enter Password: ")
    if user_name_attempt == username and password_attempt == password:
        print("Logged in by " + username)
        dashboard.profile(name, username, phone, email, password)
    elif user_name_attempt == username and password_attempt != password:
        print("Username " + username.upper() + " Found but " + password + " did not match")
        print("\nDid you forgot your password?")
    else:
        print("Those entry doesn't make sense")
