# Word2Vec_Nathan
Test d'utilisation de word2Vec avec différent corpus/modèle de BERT

# Application/modèle requis :
- Code ouvrable sur n'importe quel IDE python
- pip install gensim nltk (biblitohèque de word2vec et de tokénisation)

On peut utiliser le modèle pré-créer pour ne pas avoir besoin de générer le tout.
- pip install transformers
- pip install torch

Ils permettent d'utiliser les modèles de BERT

# modele_camemBERT
Il renvoie une valeur d'écart entre une paire de mot, malheureusement on ne peut pas l'utiliser comme écart pour déterminer
un antonyme d'un mot en partant d'un mot donné.

# modèle pré-fait cc.fr.300.bin
Le problème c'est que le modèle fait 2M de vecteurs de + de 300 dimensions, donc il est trop gros pour être charger.
