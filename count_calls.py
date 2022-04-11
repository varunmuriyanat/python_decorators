from decorators import count_calls, cache
import functools

@count_calls
def say_whee():
    print("Whee!")

@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

say_whee()
say_whee()
say_whee()
say_whee()
say_whee()


print(fibonacci(10))

# print(fibonacci.num_calls)


@functools.lru_cache(maxsize=4)
def fibonacci2(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci2(num - 1) + fibonacci2(num - 2)

print(fibonacci2(10))
print(fibonacci2(8))
print(fibonacci2(5))

print(fibonacci2.cache_info())


