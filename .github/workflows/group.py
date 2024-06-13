import re

# Read the input file
with open('./Master.m3u', 'r') as file:
    lines = file.readlines()

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

# Write the output to a new file
with open('./Master.m3u', 'w') as file:
    file.writelines(output_lines)

print("Processing complete. The modified file is saved as './Master.m3u'.")
