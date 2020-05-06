import login


# registration code
def register():
    print("Enter Your Details To Complete Your Registration")
    name = input("Enter Your Name: ")
    username = input("Choose a Unique Username: ")
    phone = input("Provide a Valid Mobile Number: ")
    email = input("Provide a valid Email Address: ")
    password = input("Create a Strong Password: ")
    confirm_password = input("Repeat Password: ")
    if confirm_password == password:
        confirm_information(name, username, phone, email, password)
    else:
        print("We could not complete your registration right now, "
              "there is an error in your details(Password). Try Again"
              )
        register()


# Function That make the user to confirm their information
def confirm_information(name, username, phone, email, password):
    print(
          "Are you sure about your information?\n"
          + "name:" + " " + name.upper()
          + "\nusername:" + " " + username
          + "\nphone number:" + " " + phone
          + "\nEmail:" + " " + email
    )
    user_response = input("Y or yes or N or no: ")
    if user_response.lower() == "y" or "yes":
        success(name, username, phone, email, password)
    else:
        welcome.front_door()


# Successful registration
def success(name, username, phone, email, password):
    print("Your registration was successful. proceed to login with the following details"
          "\n Username:" + " " + username
          + "\n Password:" + " " + password
          )
    login.login_area(name, username, phone, email, password)
    return password
