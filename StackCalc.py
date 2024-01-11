#class StackCalc: a class that extends (inherit) the functionalities
# of the class Stack 

from Stack import *
import copy
import numpy as np # if you need sin, just do np.sin, etc.

class StackCalc(Stack):
    # constructor
    def __init__(self):
        super().__init__()

    # method to perform various actions based on input string
    def rpnCommand(self, command):
        if command.isdigit() or (command[0] == '-' and command[1:].isdigit()):
            # If the command is a number, push it to the stack
            self.push(float(command))
        elif command in ['+', '-', '*', '/', '^']:
            # Basic arithmetic operations require at least 2 items in the stack
            if self.getSize() >= 2:
                num2 = self.pop()
                num1 = self.pop()
                if command == '+':
                    self.push(num1 + num2)
                elif command == '-':
                    self.push(num1 - num2)
                elif command == '*':
                    self.push(num1 * num2)
                elif command == '/':
                    self.push(num1 / num2)
                elif command == '^':
                    self.push(num1 ** num2)
        elif command.lower() in ['sin', 'cos', 'exp', 'log', 'abs', 'sqrt']:
            # Basic functions require a non-empty stack
            if not self.isEmpty():
                num = self.pop()
                if command.lower() == 'sin':
                    self.push(np.sin(num))
                elif command.lower() == 'cos':
                    self.push(np.cos(num))
                elif command.lower() == 'exp':
                    self.push(np.exp(num))
                elif command.lower() == 'log':
                    self.push(np.log(num))
                elif command.lower() == 'abs':
                    self.push(abs(num))
                elif command.lower() == 'sqrt':
                    self.push(np.sqrt(num))
        elif command.lower() in ['pi', 'e']:
            # Basic constants
            if command.lower() == 'pi':
                self.push(np.pi)
            elif command.lower() == 'e':
                self.push(np.e)
        elif command == 'swap':
            # Swap the top with the top-1 item
            self.swap()
        elif command == 'copy':
            # Duplicate the top item
            self.copy()
        elif command == 'flush':
            # Empty the stack
            self.flush()
        # Add more conditions for additional commands as needed

    # method to convert postfix expression to infix
    @staticmethod
    def postfix2infix(postfix_queue):
        # Use a stack to keep track of operands
        operand_stack = Stack()

        # Copy the postfix_queue since we need to operate on it
        postfix_copy = copy.deepcopy(postfix_queue)

        while postfix_copy.size() > 0:
            # Dequeue the next symbol from the queue
            symbol = postfix_copy.dequeue()

            try:
                # Check if the symbol is an operand 
                operand = float(symbol)
                  
                operand_stack.push(symbol)
            except ValueError:
                # The symbol is an operator
                if symbol.lower() in ['sin', 'cos', 'exp', 'log', 'abs', 'sqrt']:
                    # Handle basic functions
                    if operand_stack.getSize() >= 1:
                        value = operand_stack.pop()
                        result = f'{symbol.lower()}({value})'
                        operand_stack.push(result)
                elif symbol.lower() in ['pi', 'e']:
                    # Handle basic constants
                    operand_stack.push(symbol.lower())
                elif symbol == 'swap':
                    # Handle swap
                    operand_stack.swap()
                elif symbol.lower() == 'x':
                    operand_stack.push(symbol)
                elif symbol == 'copy':
                    # Handle copy
                    operand_stack.copy()
                elif symbol == 'flush':
                    # Handle flush
                    operand_stack.flush()
                elif symbol == '^':
                    # Handle '^' symbol
                    if operand_stack.getSize() >= 2:
                        y = operand_stack.pop()
                        x = operand_stack.pop()
                        result = f'({x})**{y}'
                        operand_stack.push(result)
                else:
                    # Handle other basic arithmetic operations
                    if operand_stack.getSize() >= 2:
                        num2 = operand_stack.pop()
                        num1 = operand_stack.pop()
                        result = f'({num1} {symbol} {num2})'
                        operand_stack.push(result)

        # The infix notation is the one at the top of the operand_stack
        return operand_stack.peek()
    
    
    @staticmethod
    def evaluate_postfix(postfix_queue, variables=None):
        operand_stack = StackCalc()
        postfix_copy = copy.deepcopy(postfix_queue)

        while postfix_copy.size() > 0:
            symbol = postfix_copy.dequeue()

            if symbol.lower() == 'x':
                if variables and 'x' in variables:
                    x_value = variables['x']
                    operand_stack.push(x_value)
                else:
                    raise ValueError("Value for 'x' is not provided.")
            elif symbol.isdigit() or (symbol[0] == '-' and symbol[1:].isdigit()):
                operand_stack.push(float(symbol))
            else:
                operand_stack.rpnCommand(symbol)

        return operand_stack.peek()




