import re

# Define marker and file paths
marker = "##########RADIO#########"
input_file = "./m3u/Kiki.m3u"
output_file = "./m3u/Kiki.m3u"

# Function to remove content after the marker
def remove_content_after_marker(content, marker):
    output = []
    for line in content:
        output.append(line)
        if marker in line:
            break
    return output

# Function to update the URLs in the content
def update_urls(content, url_mapping):
    updated_content = []
    for line in content:
        updated_line = line
        for old_url, new_url in url_mapping.items():
            updated_line = re.sub(re.escape(old_url), new_url, updated_line)
        updated_content.append(updated_line)
    return updated_content

# URL mapping
url_mapping = {
    "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg00640-lydnetwork-tayoplus-dash-sooka%2Ffc5c0f91-0841-4617-ae0a-70b09c398b38%2Findex.mpd&streamId=amg00640-lydnetwork-tayoplus-dash-sooka&sessionId=fc5c0f91-0841-4617-ae0a-70b09c398b38": "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg00640-lydnetwork-tayoplus-dash-sooka%2Ffc5c0f91-0841-4617-ae0a-70b09c398b38%2Findex.mpd",
    "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg00047-tastemade-tastemadeintlaus-dash-sooka%2F8fb9e195-d8df-45cf-9d4e-f580ac309819%2Findex.mpd&streamId=amg00047-tastemade-tastemadeintlaus-dash-sooka&sessionId=8fb9e195-d8df-45cf-9d4e-f580ac309819": "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg00047-tastemade-tastemadeintlaus-dash-sooka%2F8fb9e195-d8df-45cf-9d4e-f580ac309819%2Findex.mpd",
    "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg01077-gustoworldwidem-gustotv-dash-sooka%2F0da8c749-6a45-4a47-bbd0-db1b3198aea7%2Findex.mpd&streamId=amg01077-gustoworldwidem-gustotv-dash-sooka&sessionId=0da8c749-6a45-4a47-bbd0-db1b3198aea7": "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg01077-gustoworldwidem-gustotv-dash-sooka%2F0da8c749-6a45-4a47-bbd0-db1b3198aea7%2Findex.mpd",
    "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg01324-infamousmedia-infamoustv-dash-sooka%2F812787d9-eb16-4659-984c-f00e9e78fab1%2Findex.mpd&streamId=amg01324-infamousmedia-infamoustv-dash-sooka&sessionId=812787d9-eb16-4659-984c-f00e9e78fab1": "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg01324-infamousmedia-infamoustv-dash-sooka%2F812787d9-eb16-4659-984c-f00e9e78fab1%2Findex.mpd",
    "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg01944-ktalpha-kpopcorn-dash-sooka%2Fe015fac7-f194-4a8b-ab6d-29611e5d95f5%2Findex.mpd&streamId=amg01944-ktalpha-kpopcorn-dash-sooka&sessionId=e015fac7-f194-4a8b-ab6d-29611e5d95f5": "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg01944-ktalpha-kpopcorn-dash-sooka%2Fe015fac7-f194-4a8b-ab6d-29611e5d95f5%2Findex.mpd",
    "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg00545-edgenetworks-edgesport-dash-sooka%2Fff5558aa-63a2-4d02-a420-8b0dd3daaf16%2Findex.mpd&streamId=amg00545-edgenetworks-edgesport-dash-sooka&sessionId=ff5558aa-63a2-4d02-a420-8b0dd3daaf16": "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg00545-edgenetworks-edgesport-dash-sooka%2Fff5558aa-63a2-4d02-a420-8b0dd3daaf16%2Findex.mpd",
    "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg01570-carbontv-carbontv-dash-sooka%2Ff6317a4f-c646-47f9-8653-db9630c65bea%2Findex.mpd&streamId=amg01570-carbontv-carbontv-dash-sooka&sessionId=f6317a4f-c646-47f9-8653-db9630c65bea": "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg01570-carbontv-carbontv-dash-sooka%2Ff6317a4f-c646-47f9-8653-db9630c65bea%2Findex.mpd",
    "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg00877-b4unetworkeurop-bollywoodprime-dash-sooka%2F7c63a108-0f2c-490b-8ba9-6a3db003605f%2Findex.mpd&streamId=amg00877-b4unetworkeurop-bollywoodprime-dash-sooka&sessionId=7c63a108-0f2c-490b-8ba9-6a3db003605f": "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg00877-b4unetworkeurop-bollywoodprime-dash-sooka%2F7c63a108-0f2c-490b-8ba9-6a3db003605f%2Findex.mpd",
    "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg00223-unisysinfo-yrf-music-dash-sooka%2Fc5b25b3f-d0eb-4bb4-a763-aed528a06db0%2Findex.mpd&streamId=amg00223-unisysinfo-yrf-music-dash-sooka&sessionId=c5b25b3f-d0eb-4bb4-a763-aed528a06db0": "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg00223-unisysinfo-yrf-music-dash-sooka%2Fc5b25b3f-d0eb-4bb4-a763-aed528a06db0%2Findex.mpd",
    "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg00303-televisionkorea-estv-dash-sooka%2Fb8fecf6f-c6bf-44e4-9d55-bf5cf71b75fd%2Findex.mpd&streamId=amg00303-televisionkorea-estv-dash-sooka&sessionId=b8fecf6f-c6bf-44e4-9d55-bf5cf71b75fd": "https://cdn-apse1-prod.tsv2.amagi.tv/beacon?rp=https%3A%2F%2Fcdn-apse1-prod.tsv2.amagi.tv%2Flinear%2Famg00303-televisionkorea-estv-dash-sooka%2Fb8fecf6f-c6bf-44e4-9d55-bf5cf71b75fd%2Findex.mpd"
}

# Function to perform replacements
#def replace_content(content):
#    replacements = {
#        r'#EXTGRP:Family/Kids': 'group-title="Family/Kids 2"',
#        r'#EXTGRP:News/World': 'group-title="News/World 2"',
#        r'#EXTGRP:Variety': 'group-title="Variety 2"',
#        r'#EXTGRP:Movies': 'group-title="Movies 2"',
 #       r'#EXTGRP:Sports': 'group-title="Sports 2"',
#        r'#EXTGRP:Radio': 'group-title="Radio 2"',
 #       r'#EXTGRP:\[\*\] PLUS: SEA\'s FTA Channels': 'group-title="FTA Channels 2"'
 #   }
 #   content_str = ''.join(content)
 #   for old, new in replacements.items():
 #       content_str = re.sub(old, new, content_str)
 #   return content_str.splitlines(keepends=True)

# Function to remove specific lines matching a pattern
#def remove_lines_by_pattern(content, pattern):
#    return [line for line in content if not re.search(pattern, line)]

# Read the input file
with open(input_file, "r") as file:
    lines = file.readlines()

# Remove content after the marker
lines = remove_content_after_marker(lines, marker)

# Update the URLs in the content
lines = update_urls(lines, url_mapping)

# Remove lines containing "#KODIPROP:inputstream.adaptive.manifest_type=dash"
# lines = remove_lines_by_pattern(lines, r'#KODIPROP:inputstream\.adaptive\.manifest_type=dash')

# Perform replacements
# lines = replace_content(lines)

# Write the output to the same file
with open(output_file, "w") as file:
    file.writelines(lines)
