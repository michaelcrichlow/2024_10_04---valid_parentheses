def valid_parentheses(s: str) -> bool:
    stack = []  # initialize an empty stack (we use a list as a stack)
    # as such the only methods we'll be usign are append() and pop()

    # loop through each character in the string
    for val in s:
        if val == "(" or val == "{" or val == "[":
            stack.append(val)
        else:
            if len(stack) == 0 or \
                (val == ")" and stack.pop() != "(") or \
                (val == "}" and stack.pop() != "{") or \
                    (val == "]" and stack.pop() != "["):
                return False

    # if the stack is empty then the string was valid

    return len(stack) == 0


def main() -> None:
    value = 0
    print('value: ', value)
    print('type(value): ', type(value))


if __name__ == '__main__':
    main()
