from gensim import models

w = models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

#guess a word, find all words given distance away, guess one, repeat
possible = list(w.key_to_index.keys())
g = input("First, guess a word, input it to semantle.com, then type it here: ")
d = input("What was the similarity score? : ")
while(float(d) != float(100)):
    d = float(d)
    new_pos = []
    for key in possible:
        if abs((w.similarity(g,key)*100) - d) < 0.01:
            new_pos.append(key)
    g = new_pos[0]
    print(f'New best guess: {g}')
    possible = new_pos
    d = input("What was the similarity score? : ")