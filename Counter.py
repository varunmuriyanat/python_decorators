class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")

counter = Counter()
counter()
counter()
counter()

print(f"Counter count is {counter.count}")

