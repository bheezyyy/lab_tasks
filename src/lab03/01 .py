import string

def clean(text, lower=True, replace_yo=True):
    if lower: text = text.lower()
    if replace_yo: text = text.replace('ё','е').replace('Ё','Е')
    return ' '.join(text.replace('\n', ' ').replace('\t', ' ').split())

def split_words(txt):
    valid = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + string.ascii_lowercase + string.digits
    return ' '.join([c if c in valid else ' ' for c in txt]).split()

def word_freq(tokens):
    return {w: tokens.count(w) for w in set(tokens)}

def top_words(freq, n=5):
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]

# Teste
print(clean("  exemplo  de   texto "))
print(split_words("texto 😀 emoji"))
print(word_freq(["a", "b", "a"]))
print(top_words({'a': 2, 'b': 1}))