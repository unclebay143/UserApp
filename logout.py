# import welcome
import registration as r


# Logged the user out and back to frontdoor
def log_out():
    # getting error about circular import
    # welcome.front_door()
    # so leading to  register
    r.register()
