import parse_transcriptions
import stopwords

parsedtranscription = parse_transcriptions.parsetranscriptions()
print stopwords.removestopwords(parsedtranscription)

#gtaa