def removestopwords(query):

    file = 'dutch_stopwords.txt'
    with open(file) as f:
        lines = [line.rstrip('\n') for line in open(file)]
    querywords = query.split()

    resultwords  = [word for word in querywords if word.lower() not in lines]
    result = ' '.join(resultwords)
    return result