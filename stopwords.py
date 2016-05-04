query = 'What is hello if ed een hier hierin i can is isb'
file = 'dutch_stopwords.txt'
with open(file) as f:
    lines = [line.rstrip('\n') for line in open(file)]
querywords = query.split()

resultwords  = [word for word in querywords if word.lower() not in lines]
result = ' '.join(resultwords)

print result