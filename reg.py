from decorators import register, randomly_greet

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


randomly_greet("Varun")
