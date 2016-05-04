import wikipedia #use the wikipedia package
wikipedia.set_lang("nl") #set to dutch wikipedia only

query = "Berlage"
page = wikipedia.page(query)
#try:  print wikipedia.summary(query)
#except wikipedia.exceptions.DisambiguationError as e:
#   print e.options
#collect words that link to other pages
numberOfLinks = len(page.links)
current = 0
while current < numberOfLinks:
    print page.links[current]
    current += 1
