from transformers import AutoTokenizer, AutoModel
import torch
from torch.nn.functional import cosine_similarity
from statistics import mean


tokenizer = AutoTokenizer.from_pretrained("camembert-base")
model = AutoModel.from_pretrained("camembert-base")
model.eval()

relations = {
    "antonym": [("aube", "crépuscule"), ("chaud", "froid"), ("eau", "feu"), ("léger", "lourd")],
    # "synonym": [("canapé", "sofa"), ("rapide", "vite")],
    # "hypernym": [("animal", "chat"), ("fruit", "pomme")],
    # ... pour chaque type de relation
}

def embed_word(word):
    with torch.no_grad():
        inputs = tokenizer(word, return_tensors="pt")
        outputs = model(**inputs)
        # outputs.last_hidden_state : [batch, tokens, hidden_size]
        hidden = outputs.last_hidden_state[0]
        # moyenne des vecteurs des sous-tokens (hors [CLS], [SEP])
        return hidden[1:-1].mean(dim=0)


def cosine_dist(vec1, vec2):
    # distance = 1 - similarité
    return 1 - cosine_similarity(vec1.unsqueeze(0), vec2.unsqueeze(0)).item()


def moyenne_par_relation(relations):
    resultats = {}
    for relation, pairs in relations.items():
        dists = []
        for w1, w2 in pairs:
            v1, v2 = embed_word(w1), embed_word(w2)
            dists.append(cosine_dist(v1, v2))
        resultats[relation] = mean(dists)
    return resultats

distances = moyenne_par_relation(relations)
print(distances)

