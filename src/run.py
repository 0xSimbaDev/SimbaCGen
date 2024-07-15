from parser.parser import parse_json
from code_generator.c_generator import generate_c_code

#Load JSON data 
with open("function_declaration.json", "r") as file:
    json_str = file.read()

func_decl = parse_json(json_str)
c_code = generate_c_code(func_decl)

#Output C file name
output_file_name = "generated_function.c"

#Write C code to the file
with open(output_file_name, "w") as output_file:
    output_file.write(c_code)

print(f"C code successfully written to {output_file_name}")
