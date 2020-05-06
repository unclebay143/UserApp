import dashboard
import recover_password


# login function
def login_area(name, username, phone, email, password, security_pin, security_question):
    print("\n LOGIN AREA ")
    user_name_attempt = input("Enter Username: ")
    password_attempt = input("Enter Password: ")
    if user_name_attempt == username and password_attempt == password:
        print("Logged in as " + username.upper())
        dashboard.profile(name, username, phone, email, password, security_pin, security_question)
        # return password
    elif user_name_attempt == username and password_attempt != password:
        print("\nUsername " + username.upper() + " Found but " + password_attempt + " did not match")
        print("\nDid you forgot your password? Press F")
        confirm_forgot = input("")
        if confirm_forgot.lower() == "f":
            recover_password.confirm_user(name, username, phone, email, password, security_pin, security_question)
        login_area(name, username, phone, email, password, security_pin, security_question)
    else:
        print("\nThose entries doesn't make sense")
        login_area(name, username, phone, email, password, security_pin, security_question)
