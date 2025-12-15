from gensim.models.fasttext import FastText

model = FastText.load_facebook_vectors("cc.fr.300.bin", limit=200000)