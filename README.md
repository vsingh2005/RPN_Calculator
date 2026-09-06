# RPN Calculator

A Reverse Polish Notation (RPN) mathematical expression parser, infix-to-postfix translator, and stack-based calculation engine.

## Overview

Traditional mathematical notation (infix, such as `3 + 4 * 2`) relies on operator precedence rules and parentheses. Reverse Polish Notation (postfix, such as `3 4 2 * +`) places operators after their operands, enabling unambiguous, linear-time evaluation without recursive parsing.

This project implements custom fundamental data structures and Dijkstra's Shunting-yard algorithm to parse, translate, and evaluate arithmetic expressions interactively.

## Features

- **Infix to Postfix Translation**: Parses standard mathematical expressions into RPN using Dijkstra's Shunting-yard algorithm.
- **Linear-Time Evaluation**: Computes results in single-pass O(N) time using an operand evaluation stack.
- **Custom Data Structures**: Implements pure Python `Stack` (LIFO) and `Queue` (FIFO) data structures from scratch.
- **Interactive GUI**: Built-in graphical calculator interface for expression input and step-by-step evaluation.

## Tech Stack

- **Language**: Python 3
- **GUI Framework**: Tkinter
- **Algorithms**: Shunting-Yard Algorithm, Stack-Based Evaluation

## Project Structure

```
RPN_Calculator/
├── Stack.py        # Custom LIFO Stack implementation
├── Queue.py        # Custom FIFO Queue implementation
├── rpn.py          # Shunting-yard parser & infix-to-postfix translator
├── StackCalc.py    # Stack evaluation engine & GUI interface
└── README.md
```

## Getting Started

```bash
# Clone repository
git clone https://github.com/vsingh2005/RPN_Calculator.git
cd RPN_Calculator

# Run calculator application
python StackCalc.py
```