

def countdown(n):
    for i in range(n, -1, -1):
        yield i


n = int(input("Enter a number: "))
print(list(countdown(n)))

# Enter a number: 10
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

