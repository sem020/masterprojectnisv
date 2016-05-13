import xml.etree.cElementTree as ET
tree = ET.parse('transcriptions/transcription1.xml')
root = tree.getroot()
#print root.tag
transcription = ''
for elem in tree.iter():
    #print elem.tag
    if elem.tag == '{http://instituut.beeldengeluid.nl/namespace/iMMix}wordsequence':
        if elem.text is not None and elem.text.strip():
            transcription += elem.text + ' '
            #print '%s' % elem.text
def parsetranscriptions():
    return transcription

