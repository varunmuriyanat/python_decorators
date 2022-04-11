from decorators import singleton

@singleton
class TheOne:
    pass


first = TheOne()
anotherOne = TheOne()


print(id(first))
print(id(anotherOne))

