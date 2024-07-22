from lxml import etree

# Load the XML files
tree1 = etree.parse('./EPG/My.xml')
root1 = tree1.getroot()

tree2 = etree.parse('./EPG/Astro.xml')
root2 = tree2.getroot()

tree3 = etree.parse('./EPG/SG.xml')
root3 = tree3.getroot()

tree4 = etree.parse('./EPG/CHN.xml')
root4 = tree4.getroot()

# Function to merge one root into another
def merge_roots(root_from, root_to):
    for elem in root_from:
        root_to.append(elem)

# Merge Astro.xml into My.xml
# merge_roots(root2, root1)

# Merge SG.xml into My.xml
merge_roots(root3, root1)

# Merge CHN.xml into My.xml
merge_roots(root4, root1)

# Write the merged tree to a new file
tree1.write('./EPG/EPG.xml', pretty_print=True, xml_declaration=True, encoding='UTF-8')

