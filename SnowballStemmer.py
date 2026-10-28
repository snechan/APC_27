from nltk.stem import SnowballStemmer

ss = SnowballStemmer("english")

print(ss.stem("playing"))
print(ss.stem("running"))
print(ss.stem("starting"))