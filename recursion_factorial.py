def fact(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * fact(x - 1)


print(fact(5))
print()
print(fact(3))
print()
print(fact(1))
print(fact(0))