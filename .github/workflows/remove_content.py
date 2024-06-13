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

# Pattern to match the #EXTINF line with attributes
extinf_pattern = re.compile(r'(#EXTINF:-1)(.*?)(,.*)')
group_title_pattern = re.compile(r'(group-title="[^"]*")')

output_lines = []

for i in range(len(lines)):
    line = lines[i].strip()
    
    if line.startswith("#EXTINF:-1"):
        next_line = lines[i + 1].strip()
        
        if group_title_pattern.search(next_line):
            # Extract the group-title value
            group_title = group_title_pattern.search(next_line).group(1)
            
            # Remove group-title from the next line
            next_line = group_title_pattern.sub('', next_line).strip()
            
            # Update the #EXTINF line
            extinf_match = extinf_pattern.match(line)
            if extinf_match:
                updated_line = f"{extinf_match.group(1)} {group_title}{extinf_match.group(2)}{extinf_match.group(3)}"
                output_lines.append(updated_line + "\n")
            else:
                output_lines.append(line + "\n")
            
            # Add the cleaned next line
            output_lines.append(next_line + "\n")
        else:
            output_lines.append(line + "\n")
    elif not group_title_pattern.search(line):
        output_lines.append(line + "\n")


# Write the output to the same file
with open(output_file, "w") as file:
    file.writelines(lines)
