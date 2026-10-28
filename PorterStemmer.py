from nltk.stem import PorterStemmer

ps = PorterStemmer()

print(ps.stem("playing"))
print(ps.stem("runs"))
print(ps.stem("starting"))