import registration


# Recover Password using security question
def confirm_user(name, username, phone, email, password, security_pin, security_question):
    attempt_question = input("\nProvide Answer to the Security Question: ")
    if attempt_question == security_pin:
        print("Your Current Password is: " + password)
        login.login_area(name, username, phone, email, password, security_pin, security_question)
    else:
        print("I do not understand you...")
        registration.register()
