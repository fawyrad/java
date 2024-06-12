# remove_content.py
marker = "##########VOD#########"
input_file = "./Master.m3u"
output_file = "./Master.m3u"

with open(input_file, "r") as file:
    lines = file.readlines()

with open(output_file, "w") as file:
    for line in lines:
        file.write(line)
        if marker in line:
            break
