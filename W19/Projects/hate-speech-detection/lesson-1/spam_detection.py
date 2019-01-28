from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

CORPUS = [] ## TODO: Make sample corpus
y = []      

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(CORPUS) ## TODO: Break down fit and transform stages

classifier = MultinomialNB() 
classifier.fit(X, y)

print(classifier.predict([])) ## TODO: Create a simple test message
