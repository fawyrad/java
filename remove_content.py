# remove_content.py
marker = "##########VOD#########"
input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

with open(output_file, "w") as file:
    for line in lines:
        file.write(line)
        if marker in line:
            break
