def functions(func):
    def decorator():
        print(f"Load 1%\nLoad 64%\nLoad 99%")
        func()
        print(f"Successful")
    return decorator

def printer():
    print(f"Welcome To Advance Topic")

result = functions(printer)
result()