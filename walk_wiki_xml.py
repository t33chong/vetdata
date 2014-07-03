from corenlp_xml.document import Document

with open('/data/wiki_xml/831/description_txt.xml') as f:
    xml = f.read()

doc = Document(xml)
print doc
for sentence in doc.sentences:
    print [token.word for token in sentence.tokens]
