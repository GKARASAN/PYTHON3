def FactRecu(a):
    if a == 0:
        return 1
    return a * FactRecu(a-1)

Result = FactRecu(5)
print(Result)