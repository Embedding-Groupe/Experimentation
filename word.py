from gensim.models import Word2Vec
# model = Word2Vec.load("word2vec.model")

sentences = [
    ["le", "chat", "mange", "une", "souris"],
    ["le", "chien", "aboie","pendant","que", "le", "cheval", "dort"],
    ["le", "chat", "dort"]
]

model = Word2Vec(
    sentences,            # votre corpus
    vector_size=100,      # dimension des vecteurs (embedding)
    window=5,             # taille du contexte
    min_count=1,          # ignore les mots apparaissant moins de 1 fois
    workers=4,            # nombre de threads
    sg=0                  # 0 = CBOW, 1 = Skip-gram
)

vector = model.wv["cheval"]
print(vector.shape)

print(model.wv.similarity("chat", "chien"))

# model.save("word2vec.model")
# # Pour recharger :

