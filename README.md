# SimbaCGen: Simplify C Code Creation with JSON

This Python project streamlines the process of generating C Code from structured JSON input.

## Key Features

- **No-Code/Low-Code Approach:** Design C functions without writing C code directly.
- **JSON-Driven:** Describe the code structure in a clear, standardized format.
- **Lexical Analysis and Parsing:**  Ensures correct JSON syntax and builds an internal representation for code generation.
- **Flexible:** Easily extendable to support more complex C language features.

## How It Works

1.  **Input:**  The script takes a JSON file (`function_declaration.json` by default) as input. The JSON should describe the structure of the C function, including:

    *   `functionName`: The name of the function.
    *   `returnType`: The data type returned by the function.
    *   `arguments`: An array of objects describing the function's parameters (each with `name` and `type`).
    *   `block`: An array of objects representing the statements within the function body (e.g., variable declarations, assignments, return statements).

2.  **Lexical Analysis:** The script uses a lexer built with PLY (`lex`) to tokenize the JSON input. This breaks down the JSON into a stream of tokens like `LBRACE`, `STRING`, `NUMBER`, `INT`, etc., making it easier for the parser to understand.

3.  **Parsing:** The parser, also built with PLY (`yacc`), analyzes the token stream based on a defined grammar. If the JSON structure is valid according to the grammar, the parser builds an Abstract Syntax Tree (AST) representing the function's structure.

4.  **Code Generation:** The script then traverses the AST and generates the corresponding C code based on the information in each node. This process handles variable declarations, assignments, expressions, and other C language constructs.

## Requirements

*   **Python:** (version 3.6 or later)
*   **PLY:** Install using `pip install ply`
