# RPN Calculator

Postfix and infix expression translator and stack calculator in Python.

## Overview

Implements Dijkstra's Shunting-yard algorithm to parse infix mathematical expressions into Reverse Polish Notation (postfix) and evaluate them in linear time using an operand stack.

## Implementation Details

- **Shunting-Yard Parser**: Handles operator precedence, associativity, and parenthetical sub-expressions.
- **Stack Evaluation**: Single-pass evaluation over tokenized postfix queues.
- **Custom Stack & Queue**: Built from scratch without relying on external collections.
- **GUI Interface**: Tkinter frontend for step-by-step expression evaluation.

## Tech Stack

Python, Tkinter