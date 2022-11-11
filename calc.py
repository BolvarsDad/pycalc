#!/usr/bin/env python3

# Really only here because the assignment requires word inputs and
# to make printing expressions easier.
# Another way of doing this would be to use lambda expressions here,
# e.g. "add": lambda a,b: print(f"{a} + {b} = {a+b}"),
# in which case the input checks could be simplified to if op in ops: op(a,b)
# I dislike that approach.
ops = {
        "add": '+',
        "sub": '-',
        "mul": '*',
        "div": '/'
}

# I thought it was a more readable decision to define a helper function rather
# than having it as a standalone print statement. Plus it declares what the text is for.
def gui_help():
    print(
        "┌───────┬─────────────────────────┐\n"
        "│  add  │ Add two numbers.        │\n" 
        "│  sub  │ Subtract two numbers.   │\n"
        "│  mul  │ Multiply two numbers.   │\n"
        "│  div  │ Divide two numbers.     │\n"
        "│  exit │ Exits the program.      │\n"
        "└───────┴─────────────────────────┘"
    )

while True:
    # To achieve the same effect as the sandbox environment where the terminal screen
    # gets cleared on every iteration, you could import the os module and do a syscall
    # to clear the terminal window here, but I don't see a reason to import a whole module
    # for an aesthetic difference.
    gui_help()

    op = input("Selection > ")

    if op in ops:
        print(f"Calculating 'c' for expression:\n\ta {ops[op]} b = c\nPlease enter values for 'a' and 'b'.")
    
    elif op == "exit":
        print("Exiting the program")
        break
    
    else:
        print(f"Invalid operator '{op}' provided.")
        input("Press anything to continue")
        continue

    a = int(input("a = "))
    b = int(input("b = "))

    match op:
        case "add": print(f"{a} + {b} = {a+b}")

        case "sub": print(f"{a} - {b} = {a-b}")

        case "mul": print(f"{a} * {b} = {a*b}")

        # The demo doesn't explicitly do this but I decided to clamp the result at two decimal places.
        case "div": print(f"{a} / {b} = {a/b:.2f}")

    input("Press anything to continue.")
