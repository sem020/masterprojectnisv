import xml.etree.cElementTree as ET
tree = ET.parse('transcriptions/transcription1.xml')
root = tree.getroot()
print root.tag
for elem in tree.iter():
    print elem.tag, elem.attrib
for elem in tree.iter(tag='wordsequence'):
    print elem.text
print 'imaz'
