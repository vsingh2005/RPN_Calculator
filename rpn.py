from StackCalc import *
from Queue import *
from numpy import *  # if you need sin, just do sin, etc.
import matplotlib.pyplot as plt


# Menu
print()
print("===============================================")
print("================= Project 1 ===================")
print("===============================================")
print("|                                             |")
print("|         1-Simple  RPN calculator            |")
print("|         2-Fancy   RPN calculator            |")
print("|         3-Fancier RPN calculator            |")
print("|                                             |")
print("===============================================")
print()
choice=input("Your choice: ")


mystack=StackCalc()
myqueue=Queue()

if __name__ == "__main__":
    mystack = StackCalc()
    myqueue = Queue()


if choice=="1": #////////////// Simple RPN calculator

    print("Welcome to the simple RPN calculator (enter 'quit' to quit)");
    while True:
        print("----------------------------------------------------------")
        print(mystack)
        prompt=input(">")    
        if prompt=="quit": break
        mystack.rpnCommand(prompt)



if choice=="2": #////////////// Fancy RPN calculator

    print("Welcome to the fancy RPN calculator (enter 'quit' to quit)");
    while True:
        print("----------------------------------------------------------")
        print(mystack)
        if not myqueue.isEmpty(): #Display both postfix and infix
            print("Postfix: "+str(myqueue))
            print("Infix: ",StackCalc.postfix2infix(myqueue))
        prompt=input(">")    
        if prompt=="quit": break
        mystack.rpnCommand(prompt)
        if prompt!="flush":
            myqueue.enqueue(prompt)
        else:
            myqueue.flush()

        
if choice == "3":  # Fancier RPN calculator
        print("Welcome to the fancier RPN calculator (enter 'quit' to quit)")
        while True:
            print("----------------------------------------------------------")
            if not myqueue.isEmpty():  # Display both postfix and infix
                print("Postfix:", str(myqueue))
                infix_expression = StackCalc.postfix2infix(myqueue)
                print("Infix:", infix_expression)
            prompt = input(">")
            if prompt == "quit":
                break

            if prompt.isdigit() or (prompt[0] == '-' and prompt[1:].isdigit()):
                # Display postfix and infix when the user enters a number
                mystack.rpnCommand(prompt)
                myqueue.enqueue(prompt)
            elif prompt.lower() == 'x':
                # Treat 'x' as a placeholder and enqueue it in the infix expression
                myqueue.enqueue(prompt)
            elif prompt in ['+', '-', '*', '/', '^']:
                mystack.rpnCommand(prompt)
                myqueue.enqueue(prompt)
            else:
                if prompt.lower() in ['sin', 'cos', 'tan', 'exp', 'log', 'abs', 'sqrt']:
                    mystack.rpnCommand(prompt)
                    myqueue.enqueue(prompt)
                elif prompt.lower() in ['pi', 'e']:
                    mystack.rpnCommand(prompt)
                    myqueue.enqueue(prompt.lower())
                else:
                    mystack.rpnCommand(prompt)
            x_value = None
            if prompt == "run":
                if myqueue.find('x'):
                    x_value = float(input("Enter x value: "))
                    result = StackCalc.evaluate_postfix(myqueue, {'x': x_value})
                else:
                    result = StackCalc.evaluate_postfix(myqueue)

                if x_value is not None:  # Check if x_value is defined
                    # Use locals() to pass the variable 'x' into the eval function
                    local_vars = {'x': x_value}
                    print(f"Solution using infix: {eval(infix_expression, None, local_vars)}")
                else:
                    print(f"Solution using infix: {int(result)}")

                print(f"Solution using postfix: {result}")


            elif prompt == "plot" and myqueue.find('x'):
                xmin, xmax, nbp = map(float, input("Enter values of xmin, xmax, nbp: ").split())
                x_values = np.linspace(xmin, xmax, int(nbp))
                y_values = [StackCalc.evaluate_postfix(myqueue, {'x': x}) for x in x_values]
                plt.plot(x_values, y_values)
                plt.xlabel("x")
                plt.ylabel("f(x)")
                plt.title("f(x) = " + infix_expression)  # Set the title to the infix expression
                plt.show()

            elif prompt == "flush":
                myqueue.flush()

print("Thanks for using the RPN calculator")
