import login


# registration code
def register():
    print("\nEnter Your Details To Complete Your Registration\n")
    name = input("Enter Your Name: ")
    username = input("Choose a Unique Username: ")
    phone = input("Provide a Valid Mobile Number: ")
    email = input("Provide a valid Email Address: ")
    password = input("Create a Strong Password: ")
    confirm_password = input("Repeat Password: ")
    security_question = "Provide a 4 digit security pin: "
    security_pin = input(security_question)
    if len(security_pin) != 4 and len(security_pin) < 4:
        print(" Too short, 4 Required")
        register()
    elif len(security_pin) > 4:
        print(" Too Long, 4 Required")
        register()
    if confirm_password == password:
        confirm_information(name, username, phone, email, password, security_pin, security_question)
    else:
        print("\nWe could not complete your registration right now, "
              "there is an error in your details(Password). Try Again\n"
              )
        register()


# Function That make the user to confirm their information
def confirm_information(name, username, phone, email, password, security_pin, security_question):
    print(
          "\nAre you sure about your information?\n"
          + "name:" + " " + name.upper()
          + "\nusername:" + " " + username
          + "\nphone number:" + " " + phone
          + "\nEmail:" + " " + email
          + "\nSecurity Question:" + " " + security_question
          + "\nSecurity pin:" + " is secured!!!"
    )
    user_response = input("\nY for yes or N for no: ")
    if user_response.lower() == "y":
        success(name, username, phone, email, password, security_pin, security_question)
    elif user_response.lower() == "n":
        register()
    else:
        print("Sorry I didn't catch that")
        register()


# Successful registration
def success(name, username, phone, email, password, security_pin, security_question):
    print("\nYour registration was successful. proceed to login with the following details\n"
          "\n Username:" + " " + username
          + "\n Password:" + " " + password
          )
    login.login_area(name, username, phone, email, password, security_pin, security_question)
    return password
