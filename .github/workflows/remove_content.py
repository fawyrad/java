import re

def process_playlist(input_file, output_file, marker):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove content after the marker
    content_lines = content.splitlines(keepends=True)
    output_lines = []
    marker_found = False
    for line in content_lines:
        output_lines.append(line)
        if marker in line:
            marker_found = True
            break
    if marker_found:
        content = ''.join(output_lines)

    # Perform replacements
    replacements = {
        r'#EXTGRP:Family/Kids': 'group-title="Family/Kids 2"',
        r'#EXTGRP:News/World': 'group-title="News/World 2"',
        r'#EXTGRP:Variety': 'group-title="Variety 2"',
        r'#EXTGRP:Movies': 'group-title="Movies 2"',
        r'#EXTGRP:Sports': 'group-title="Sports 2"',
        r'#EXTGRP:Radio': 'group-title="Radio 2"',
        r'#EXTGRP:\[\*\] PLUS: SEA\'s FTA Channels': 'group-title="FTA Channels 2"'
    }
    for old, new in replacements.items():
        content = re.sub(old, new, content)

    

    # Regular expression to match the desired pattern for rearranging group-title
    pattern = re.compile(r'(#EXTINF:-1 .+?)(group-title="[^"]+")(.+?\nhttps[^\s]+)', re.DOTALL)
    
    # Function to rearrange the matched groups
    def rearrange(match):
        return f"{match.group(1)}{match.group(3)}\n{match.group(2)}"

    # Substitute with the rearranged pattern
    content = pattern.sub(rearrange, content)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)

# Specify the input and output file paths and the marker
input_file = './Master.m3u'
output_file = './Master.m3u'
marker = '##########VOD#########'

process_playlist(input_file, output_file, marker)
