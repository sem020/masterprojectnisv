import RDF

parser = RDF.NTriplesParser()

for triple in parser.parse_as_stream("file:./mybigNTfile.nt"):
  print triple.subject, triple.predicate, triple.object