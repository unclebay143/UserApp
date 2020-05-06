import login
import logout


# Dashboard Area
def profile(name, username, phone, email, password, security_pin, security_question):
    print("Name: " + name.upper())
    print("Username: " + username)
    print("Email: " + email)
    print("Press C to change Password")
    print("Press L to Logout")
    password_change_request = input(": ")
    if password_change_request.lower() == "c":
        password_change_request = password
        change_password(name, username, phone, email, password,
                        security_pin, security_question, password_change_request)
    if password_change_request.lower() == "l":
        logout.log_out()


# Confirm Old Password
def change_password(name, username, phone, email, password, security_pin, security_question, old_password):
    print(old_password)
    confirm_old_password = input("\nConfirm Old Password: ")
    if confirm_old_password.lower() == old_password.lower():
        password_change(name, username, phone, email, password, security_pin, security_question)
    else:
        print("\nNot correct")
        change_password(name, username, phone, email, password, security_pin, security_question, old_password)


# change Password can use parameter name change_to_new_password instead of password to clear confusions
def password_change(name, username, phone, email, password, security_pin, security_question):
    new_password = input("\nEnter New Password: ")
    print("\n One More Step")
    confirm_new_password = input("\nRepeat New Password: ")
    if new_password == confirm_new_password:
        password = new_password
        print("\n Password changed successfully. Your New Password is " + password)
        print("\nLogin Again")
        login.login_area(name, username, phone, email, password, security_pin, security_question)
