def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x - 1)

print(fat(3))

# o codigo está usando recursão para fazer o fatorial de um numero x.