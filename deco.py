from datetime import datetime

def not_during_the_night(func):
    print(datetime.now().hour)
    def wrapper():
        if 18 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)
#say_whee = my_decorator(say_whee)

say_whee()


