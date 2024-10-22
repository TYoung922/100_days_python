import operator

def mathing():
    new_oper = True
    operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv

    }
    carry_over = 0
    while new_oper:
        first_numb = int(input("What's the first number?: "))
        print("+ \n - \n * \n /")
        choose_func = input("Pick an operation: ")
        second_numb = int(input("What's the second number?: "))
        result = operators[choose_func](first_numb, second_numb)
        print(f"{first_numb} {choose_func} {second_numb} =", result)
        again = input(f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation ")
        if again == "y":
            carry_over = result
            new_oper = False

    while not new_oper:
        print("+ \n - \n * \n /")
        choose_func = input("Pick an operation: ")
        second_numb = int(input("What's the second number?: "))
        result = operators[choose_func](carry_over, second_numb)
        print(f"{carry_over} {choose_func} {second_numb} =", result)
        again = input(f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation ")
        if again == "n":
            new_oper = True
            mathing()
        else:
            carry_over = result
            new_oper = False
mathing()