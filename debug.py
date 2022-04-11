from decorators import debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

make_greeting("Varun")
make_greeting("Saya", age=8)
#make_greeting("Saya", age=8, position="middle")
