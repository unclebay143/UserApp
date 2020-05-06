import registration as r
import login


# Welcome door
def front_door():
    print("\nWelcome to Walk-In Tech Python Tutorial Course\n")
    print("Press R to register")
    print("Press L to login")
    ask = input(": ")
    if ask.lower() == "r":
        r.register()
    elif ask.lower() == "l":
        try:
            login.login_area()
        except TypeError:
            print("Service/Function Coming soon...")
            front_door()
    else:
        print("Something went wrong")
        front_door()


front_door()
