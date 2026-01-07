from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "ganhe dinheiro agora",
    "promoção imperdível",
    "reunião amanhã às 10",
    "relatório em anexo"
]

labels = [1, 1, 0, 0]  # 1 = spam, 0 = normal

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def predict(text):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]
