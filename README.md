# String Calculator

A simple calculator that sums numbers from a string with support for custom delimiters, and handles negative numbers with proper error handling.

## Description

This project implements a basic calculator that can take a string of numbers separated by commas, newlines, or custom delimiters. The calculator computes the sum of the numbers. It includes input validation to reject negative numbers and raises an error with a descriptive message listing the negative numbers encountered.

## Features
- Supports custom delimiters (e.g., `//;`).
- Handles multiple delimiters like commas and newlines.
- Raises errors if negative numbers are encountered.

## Getting Started

These instructions will guide you through setting up the project on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following prerequisites installed:

- **Python 3.x**: Ensure Python is installed on your machine.
  - Download from [python.org](https://www.python.org/downloads/).

**Supported Operating Systems**:
- Windows, macOS, and Linux.

### Installing

Follow these steps to get the project running on your machine.

1. **Clone the repository**:
    ```bash
    git clone https://github.com/anamikasingh-25git/incubyte_test.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd INCUBYTE
    ```

### Running the Program

To run the calculator program, follow these steps:

1. **Run the Python script**:
    ```bash
    python String_Calculator.py
    ```

2. **Example Usage**:

    1. **For an empty input**:
        ```python
        print(SUM1.Calculate_Sum(""))  # returns 0
        ```

    2. **For a basic input**:
        ```python
        print(SUM1.Calculate_Sum("1,5"))  # returns 6
        ```

    3. **For newline-separated numbers**:
        ```python
        print(SUM1.Calculate_Sum("1\n2,3"))  # returns 6
        ```

    4. **For a custom delimiter**:
        ```python
        print(SUM1.Calculate_Sum("//;\\n1;2"))  # returns 3
        ```

    5. **For invalid input (negative numbers)**:
        ```python
        try:
            print(SUM1.Calculate_Sum("1,2,-3,4"))
        except ValueError as ex:
            print(ex)  # prints: negative numbers not allowed: -3
        ```

### Testing

To run the unit tests for this project, use the following command:

```bash
python -m unittest test.py
