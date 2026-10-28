from nltk.stem.lancaster import LancasterStemmer

ps = LancasterStemmer()

print(ps.stem("playing"))
print(ps.stem("running"))
print(ps.stem("starting"))