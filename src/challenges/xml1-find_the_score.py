import sys
import xml.etree.ElementTree as etree

SAMPLE_LINES = 6
SAMPLE_XML = """
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
"""

def get_attr_number(node):
    attrib_list = []
    for child in node.iter():
        attrib_list.append(len(child.attrib))
    return sum(attrib_list)

if __name__ == '__main__':
    #sys.stdin.readline()
    #xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(SAMPLE_XML))
    root = tree.getroot()
    print(get_attr_number(root))