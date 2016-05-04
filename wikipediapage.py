import wikipedia #use the wikipedia package
wikipedia.set_lang("nl") #set to dutch wikipedia only
page = wikipedia.page("Hema") #gather text content of that page
print page.content
word = 'is'
if word in page:
    print('Succes!')

