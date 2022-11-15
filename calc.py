# Kalle
import os
#!/usr/bin/env python3

# Really only here because the assignment requires word inputs and
# to make printing expressions easier.
# Another way of doing this would be to use lambda expressions here,
# e.g. "add": lambda a,b: print(f"{a} + {b} = {a+b}"),
# in which case the input checks could be simplified to something like 'if op in ops: op(a,b)'
# I dislike that approach because it makes the dictionary very unreadable.
ops = {
        "add": '+',
        "sub": '-',
        "mul": '*',
        "div": '/'
}

while True:
    os.system("clear")

    print(
        "┌───────┬─────────────────────────┐\n"
        "│  add  │ Add two numbers.        │\n" 
        "│  sub  │ Subtract two numbers.   │\n"
        "│  mul  │ Multiply two numbers.   │\n"
        "│  div  │ Divide two numbers.     │\n"
        "│  exit │ Exits the program.      │\n"
        "└───────┴─────────────────────────┘"
    )

    op = input("Selection > ")
    # Kalle
    # Karam
    if op in ops:
        print(f"Calculating 'c' for expression:\n\ta {ops[op]} b = c\nPlease enter values for 'a' and 'b'.")
    
    # Having a program that never exits an infinite loop is obviously bad, so I implemented
    # 'exit' as a sentinel value the user can use to exit the program without explicitly killing it.
    elif op == "exit":
        print("Exiting the program")
        break
    
    else:
        print(f"Invalid operator '{op}' provided.")
        input("Press anything to continue")
        continue

    try:
        a = int(input("a = "))
        b = int(input("b = "))
    # Karam
    # Jasmine
    except Exception as e:
        print("Non-integer value entered as argument.")
        input("Press anything to continue")
        continue

    # The demo actually prints that division by 0 results in infinity, which is is mathematically wrong.
    if op == "div" and b == 0:
        print("Attempted division by 0.")
        input("Press anything to continue")
        continue
    # Jasmine
    # Sinan
    match op:
        case "add": print(f"{a} + {b} = {a+b}")

        case "sub": print(f"{a} - {b} = {a-b}")

        case "mul": print(f"{a} * {b} = {a*b}")

        # The demo doesn't explicitly do this but I decided to clamp the result at two decimal places.
        case "div": print(f"{a} / {b} = {a/b:.2f}")

    input("Press anything to continue.")
    # Sinan
