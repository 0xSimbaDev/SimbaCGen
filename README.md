# SimbaCGen: Simplify C Code Creation with JSON

This Python project streamlines the process of generating C code from structured JSON input.

## Key Features

- **No-Code/Low-Code Approach:** Design C functions without writing C code directly.
- **JSON-Driven:** Describe the code structure in a clear, standardized format.
- **AST-Based Parsing:** Builds an internal representation for code generation.
- **Flexible:** Easily extendable to support more complex C language features.

## How It Works

1. **Input:** The script takes a JSON string as input. The JSON should describe the structure of the C function, including:
    - `type`: Specifies the type of the JSON object, e.g., "function_declaration".
    - `name`: The name of the function.
    - `return_type`: The data type returned by the function.
    - `arguments`: An array of objects describing the function's parameters (each with `name` and `type`).
    - `block`: An array of objects representing the statements within the function body (e.g., variable declarations, assignments, return statements).

2. **Parsing:** The `parser.py` module processes the JSON input and constructs an Abstract Syntax Tree (AST). This AST represents the structure of the function in a way that the code generator can understand.

3. **Code Generation:** The `code_generator.py` module traverses the AST and generates the corresponding C code. This process handles variable declarations, assignments, expressions, and other C language constructs.

## Project Structure

```plaintext
- ast.py              # Defines the classes for the Abstract Syntax Tree (AST) nodes.
- parser.py           # Contains the code to parse the JSON input and construct the AST.
- code_generator.py   # Generates C code from the AST.
- main.py             # Main script to demonstrate the usage of the tool.
```

## Requirements

*   **Python:** (version 3.6 or later)
*   **PLY:** Install using `pip install ply`

## Example
The following is a sample JSON input that describes a simple function in C:

```
{
  "type": "function_declaration",
  "name": "nested_example",
  "return_type": "void",
  "arguments": [],
  "block": [
    {
      "type": "variable_declaration",
      "declarations": [
        {
          "name": "x",
          "type": "int",
          "value": {
            "type": "literal",
            "value": "0"
          }
        }
      ]
    },
    {
      "type": "if_statement",
      "condition": {
        "type": "binary_operation",
        "operator": "==",
        "left": {
          "type": "variable_reference",
          "name": "x"
        },
        "right": {
          "type": "literal",
          "value": "0"
        }
      },
      "then_block": [
        {
          "type": "if_statement",
          "condition": {
            "type": "binary_operation",
            "operator": ">",
            "left": {
              "type": "variable_reference",
              "name": "x"
            },
            "right": {
              "type": "literal",
              "value": "-1"
            }
          },
          "then_block": [
            {
              "type": "expression_statement",
              "expression": {
                "type": "function_call",
                "name": "printf",
                "arguments": [
                  {
                    "type": "literal",
                    "value": "\"Nested if statement\""
                  }
                ]
              }
            }
          ]
        }
      ]
    }
  ]
}

```

Running main.py with this input will generate the following C code:

```
void nested_example() {
    int x = 0;
    if (x == 0) {
        if (x > -1) {
            printf("Nested if statement");
        }
    }
}
```

## Contributing

Contributions are welcome! Feel free to submit issues and enhancement requests. Pull requests are also welcome.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

