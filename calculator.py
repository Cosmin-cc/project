from tkinter import *
from operator import add, sub, mul, truediv
import re

# Operatorii și prioritățile lor
OPERATORS = {'+': (1, add), '-': (1, sub),
             '*': (2, mul), '/': (2, truediv)}

# Conversie expresie infixată în RPN folosind Shunting Yard Algorithm
def infix_to_rpn(expression):
    output = []
    stack = []
    tokens = re.findall(r'\d+|[-+*/()]', expression)

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in OPERATORS:
            while stack and stack[-1] in OPERATORS and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    return output

# Construirea arborelui de expresii
def build_expression_tree(rpn_tokens):
    stack = []
    for token in rpn_tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in OPERATORS:
            if len(stack) < 2:
                raise ValueError("Invalid expression")
            right = stack.pop()
            left = stack.pop()
            stack.append(OPERATORS[token][1](left, right))
    return stack[0] if stack else None

# Funcția care procesează expresia și afișează rezultatul
def equalpress():
    try:
        global expression
        rpn_expr = infix_to_rpn(expression)
        result = build_expression_tree(rpn_expr)
        equation.set(str(result) if result is not None else "Error")
        expression = ""
    except Exception as e:
        equation.set("Error")
        expression = ""

# Funcții pentru operare
expression = ""
def press(num):
    global expression
    expression += str(num)  # Construiește expresia
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

# Interfață grafică
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="gray")
    gui.title("Calculator cu evaluare RPN")
    gui.geometry("340x180")

    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
    equation.set('')

    buttons = [
        ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('+', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
        ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('*', 4, 3),
        ('0', 5, 0), ('(', 5, 1), (')', 5, 2), ('/', 5, 3),
    ]

    for (text, row, col) in buttons:
        Button(gui, text=f' {text} ', fg='white', bg='blue', command=lambda t=text: press(t), height=1, width=7).grid(row=row, column=col)

    Button(gui, text=' = ', fg='black', bg='blue', command=equalpress, height=1, width=7).grid(row=6, column=2)
    Button(gui, text='Clear', fg='white', bg='blue', command=clear, height=1, width=7).grid(row=6, column=1)

    gui.mainloop()
d
