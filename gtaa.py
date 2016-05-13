from SPARQLWrapper import SPARQLWrapper, JSON
# add a default graph, though that can also be done in the query string
sparql = SPARQLWrapper("http://localhost:3020/sparql/?query")
sparql.setQuery("""SELECT * WHERE{?a ?b "Amsterdam"@nl}""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
  # the previous query as a literal string



#for result in results["results"]["bindings"]:
#    print(result["label"]["value"])
