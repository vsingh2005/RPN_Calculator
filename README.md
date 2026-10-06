# RPN Calculator & Expression Translator

A postfix (Reverse Polish Notation) and infix mathematical expression parser and evaluation engine written in Python.

## Overview

Mathematical expression evaluation requires resolving operator precedence, associativity rules, and nested parentheses. This repository implements Dijkstra's Shunting-yard algorithm to translate human-readable infix arithmetic into postfix notation, which is subsequently evaluated in linear O(N) time using a stack machine.

## Core Features

- **Infix to Postfix Translation**: Parses infix expressions and converts them to postfix tokens using Dijkstra's Shunting-yard algorithm, handling standard arithmetic operators (`+`, `-`, `*`, `/`, `^`) with correct precedence and left/right associativity.
- **Linear-Time Evaluation**: Evaluates postfix token sequences in single-pass O(N) time and O(N) space complexity using a custom evaluation stack.
- **Custom Data Structure Implementations**: Implements fundamental `Stack` and `Queue` classes with boundary checks, dynamic resizing, and explicit error handling.
- **Desktop Graphical Interface**: Includes a lightweight desktop calculator interface built with Python's native Tkinter library.

## Technology Stack

- **Language**: Python 3
- **GUI Framework**: Tkinter
- **Testing**: Pytest

## Getting Started

### Installation and Execution

```bash
git clone https://github.com/vsingh2005/RPN_Calculator.git
cd RPN_Calculator
python main.py
```