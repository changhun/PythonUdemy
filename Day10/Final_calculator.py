from art import logo


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multi(a, b):
    return a * b


def div(a, b):
    return a / b


operation_dictionary = {
    "+": add,
    '-': sub,
    '*': multi,
    '/': div
}
print(logo)


def calculator():
    first_num = float(input("What's the first number?"))
    continue_loop = True
    while continue_loop:
        for op in operation_dictionary:
            print(op)
        operation = input("Pick an operation: ")
        second_num = float(input("What's the next number?"))

        function = operation_dictionary[operation]
        answer = function(first_num, second_num)
        print(f"{first_num} {operation} {second_num} = {answer}")

        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if cont == 'y':
            first_num = answer
        else:
            continue_loop = False
            calculator()


calculator()