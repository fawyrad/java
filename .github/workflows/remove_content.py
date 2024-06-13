import re

# Define marker and file paths
marker = "##########VOD#########"
input_file = "./Master.m3u"
output_file = "./Master.m3u"

# Function to remove content after the marker
def remove_content_after_marker(content, marker):
    output = []
    for line in content:
        output.append(line)
        if marker in line:
            break
    return output

# Function to perform replacements
def replace_content(content):
    replacements = {
        r'#EXTGRP:Family/Kids': 'group-title="Family/Kids 2"',
        r'#EXTGRP:News/World': 'group-title="News/World 2"',
        r'#EXTGRP:Variety': 'group-title="Variety 2"',
        r'#EXTGRP:Movies': 'group-title="Movies 2"',
        r'#EXTGRP:Sports': 'group-title="Sports 2"',
        r'#EXTGRP:Radio': 'group-title="Radio 2"',
        r'#EXTGRP:\[\*\] PLUS: SEA\'s FTA Channels': 'group-title="FTA Channels 2"'
    }
    content_str = ''.join(content)
    for old, new in replacements.items():
        content_str = re.sub(old, new, content_str)
    return content_str.splitlines(keepends=True)

# Read the input file
with open(input_file, "r") as file:
    lines = file.readlines()

# Remove content after the marker
lines = remove_content_after_marker(lines, marker)

# Perform replacements
lines = replace_content(lines)

# Write the output to the same file
with open(output_file, "w") as file:
    file.writelines(lines)
