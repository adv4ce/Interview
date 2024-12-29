class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)


def is_balanced(sequence):
    stack = Stack()
    brackets = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for bracket in sequence:
        if bracket in brackets.values():
            stack.push(bracket)

        else:
            if not stack.is_empty() and stack.peek() == brackets[bracket]:
                stack.pop()
            else:
                return "Несбалансированно"

    return "Сбалансированно"


assert is_balanced("(((([{}]))))") == "Сбалансированно"
assert is_balanced("[([])((([[[]]])))]{()}") == "Сбалансированно"
assert is_balanced("{{[()]}}") == "Сбалансированно"

assert is_balanced("}{}") == "Несбалансированно"
assert is_balanced("{{[(])]}}") == "Несбалансированно"
assert is_balanced("[[{())}]") == "Несбалансированно"
