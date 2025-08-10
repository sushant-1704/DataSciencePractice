from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from gensim.models import Word2Vec
import numpy as np

# Dataset
data = [
    ("I love this movie, it is fantastic and thrilling", 1),
    ("This film was terrible and boring", 0),
    ("Amazing acting and wonderful story", 1),
    ("I did not like the movie, it was dull", 0),
    ("An excellent and engaging film", 1),
    ("The plot was weak and uninteresting", 0),
    ("A masterpiece with brilliant direction", 1),
    ("Not worth watching, very disappointing", 0),
    ("A great movie with stunning visuals", 1),
    ("The movie was a complete waste of time", 0),
    ("Loved the soundtrack and performances", 1),
    ("Poor script and bad acting ruined it", 0),
    ("Fantastic story with strong characters", 1),
    ("The film lacked depth and emotion", 0),
    ("Highly recommend this wonderful movie", 1),
    ("I fell asleep, it was so boring", 0),
    ("Exceptional cinematography and plot", 1),
    ("Not engaging and poorly made", 0),
    ("A beautiful film that touched my heart", 1),
    ("Terrible experience, I want my time back", 0),
]

texts, labels = zip(*data)

def preprocess(text):
    return text.lower()

texts = [preprocess(t) for t in texts]

# Feature extraction
vectorizer_uni = CountVectorizer(ngram_range=(1,1))
X_uni = vectorizer_uni.fit_transform(texts)

vectorizer_bi = CountVectorizer(ngram_range=(2,2))
X_bi = vectorizer_bi.fit_transform(texts)

tokenized_texts = [t.split() for t in texts]
w2v_model = Word2Vec(sentences=tokenized_texts, vector_size=50, window=3, min_count=1, sg=1, epochs=100)

def avg_word2vec(sentence):
    vectors = []
    for word in sentence.split():
        if word in w2v_model.wv:
            vectors.append(w2v_model.wv[word])
    if vectors:
        return np.mean(vectors, axis=0)
    else:
        return np.zeros(50)

X_w2v = np.array([avg_word2vec(s) for s in texts])

X_uni_train, X_uni_test, y_train, y_test = train_test_split(X_uni, labels, test_size=0.3, random_state=42)
X_bi_train, X_bi_test, _, _ = train_test_split(X_bi, labels, test_size=0.3, random_state=42)
X_w2v_train, X_w2v_test, _, _ = train_test_split(X_w2v, labels, test_size=0.3, random_state=42)

def train_evaluate(model, X_tr, X_te, y_tr, y_te, name, file_handle):
    model.fit(X_tr, y_tr)
    preds = model.predict(X_te)
    acc = accuracy_score(y_te, preds)
    report = classification_report(y_te, preds)
    
    file_handle.write(f"\n=== Results for {name} ===\n")
    file_handle.write(f"Accuracy: {acc:.4f}\n")
    file_handle.write(f"{report}\n")

with open("results_of_txt_classification.txt", "w", encoding="utf-8") as f:
    nb = MultinomialNB()
    train_evaluate(nb, X_uni_train, X_uni_test, y_train, y_test, "Naive Bayes (Unigram BoW)", f)

    rf = RandomForestClassifier(random_state=42)
    train_evaluate(rf, X_uni_train, X_uni_test, y_train, y_test, "Random Forest (Unigram BoW)", f)

    nb_bi = MultinomialNB()
    train_evaluate(nb_bi, X_bi_train, X_bi_test, y_train, y_test, "Naive Bayes (Bigram BoW)", f)

    rf_bi = RandomForestClassifier(random_state=42)
    train_evaluate(rf_bi, X_bi_train, X_bi_test, y_train, y_test, "Random Forest (Bigram BoW)", f)

    rf_w2v = RandomForestClassifier(random_state=42)
    train_evaluate(rf_w2v, X_w2v_train, X_w2v_test, y_train, y_test, "Random Forest (Avg Word2Vec)", f)