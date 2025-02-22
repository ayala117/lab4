def square_generator(n):
    for i in range(n + 1):
        yield i ** 2


N = int(input("Enter a number: "))
print(list(square_generator(N)))


# Enter a number: 5
# [0, 1, 4, 9, 16, 25]