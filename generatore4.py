

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


a = int(input("Enter the start value: "))
b = int(input("Enter the end value: "))

for val in squares(a, b):
    print(val)
# Enter the start value: 2
# Enter the end value: 5
# 4,9,16,25
