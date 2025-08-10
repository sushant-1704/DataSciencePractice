from gensim.models import Word2Vec

# 1. Preprocessed corpus (tokenized)
corpus = [
    ['king', 'queen', 'man', 'woman', 'royal', 'crown', 'throne'],
    ['apple', 'banana', 'fruit', 'orange', 'sweet', 'tree', 'juice'],
    ['car', 'bus', 'train', 'road', 'vehicle', 'travel', 'engine'],
    ['dog', 'cat', 'pet', 'animal', 'cute', 'tail', 'fur'],
    ['doctor', 'nurse', 'hospital', 'medicine', 'health', 'patient', 'clinic'],
    ['computer', 'laptop', 'keyboard', 'mouse', 'screen', 'technology', 'software'],
    ['river', 'water', 'fish', 'stream', 'lake', 'ocean', 'wave'],
    ['book', 'author', 'page', 'read', 'library', 'story', 'novel'],
    ['teacher', 'student', 'class', 'school', 'lesson', 'homework', 'education'],
    ['football', 'cricket', 'game', 'team', 'player', 'score', 'match'],
    ['phone', 'call', 'message', 'contact', 'mobile', 'screen', 'app'],
    ['city', 'town', 'village', 'population', 'road', 'building', 'market'],
    ['music', 'song', 'melody', 'instrument', 'guitar', 'piano', 'concert'],
    ['food', 'taste', 'cook', 'restaurant', 'meal', 'drink', 'delicious'],
    ['garden', 'flower', 'tree', 'plant', 'grass', 'leaf', 'green'],
]

# 2. Train Word2Vec Skip-Gram model
model_sg = Word2Vec(
    sentences=corpus,
    vector_size=50,
    window=2,
    min_count=1,
    sg=1,        # Skip-Gram
    epochs=100
)

with open("result_of_word2vec.txt", "w", encoding="utf-8") as f:
    # 3. Embedding vector for 'king'
    f.write("Embedding vector for 'king':\n")
    king_vector = model_sg.wv['king']
    f.write(str(king_vector) + "\n\n")

    # 4. Top 5 most similar words to 'king'
    f.write("Top 5 words similar to 'king':\n")
    similar_words = model_sg.wv.most_similar('king', topn=5)
    for word, similarity in similar_words:
        f.write(f"{word}: {similarity:.4f}\n")
    f.write("\n")

    # 5. Cosine similarity between 'king' and 'queen'
    similarity = model_sg.wv.similarity('king', 'queen')
    f.write(f"Cosine similarity between 'king' and 'queen': {similarity:.4f}\n\n")

    # 6. Train CBOW model with different parameters
    model_cbow = Word2Vec(
        sentences=corpus,
        vector_size=100,
        window=3,
        min_count=1,
        sg=0,       # CBOW
        epochs=100
    )

    f.write("Top 5 words similar to 'king' using CBOW model:\n")
    similar_words_cbow = model_cbow.wv.most_similar('king', topn=5)
    for word, similarity in similar_words_cbow:
        f.write(f"{word}: {similarity:.4f}\n")