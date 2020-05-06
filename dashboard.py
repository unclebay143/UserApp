# Dashboard Area
def profile(name, username, phone, email, password):
    print("Name: " + name)
    print("Username: " + username)
    print("Email: " + email)
    print("Press C to change Password")
    password_change_request = password
    password_change_request = input(": ")
    if password_change_request.lower() == "c":
        change_password(password_change_request)


# Confirm Old Password
def change_password(old_password):
    print(old_password)
    confirm_old_password = input("Confirm Old Password: ")
    if confirm_old_password.lower() == old_password.lower():
        password_change(old_password)
        print("Login Again")
        login.login_area(name, username, phone, email, password)
    else:
        print("not correct")


# change Password
def password_change(old_password):
    new_password = input("Enter New Password: ")
    print("\n One More Step")
    confirm_new_password = input("Repeat New Password")
    if new_password == confirm_new_password:
        old_password = new_password
        print("Password changed successfully. Your New Password is " + old_password)
        return old_password
