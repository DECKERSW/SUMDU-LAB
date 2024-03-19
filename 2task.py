import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

# Зчитування тексту з файлу з явним вказанням кодування UTF-8
with open("Randomtext.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Токенізація тексту на рівні абзаців
paragraphs = sent_tokenize(text)

# Ініціалізація стоп-слів та пунктуації
stop_words = set(stopwords.words("english"))
punctuations = set(string.punctuation + " – " + " — " + " ― ")

# Ініціалізація лематизатора та стеммера
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

processed_paragraphs = []

for paragraph in paragraphs:
    # Токенізація абзацу на слова
    tokens = word_tokenize(paragraph)
    
    # Лематизація, стеммінг та видалення стоп-слів та пунктуації
    processed_tokens = []
    for token in tokens:
        if token.lower() not in stop_words and token.lower() not in punctuations:
            lemma = lemmatizer.lemmatize(token.lower())
            stem = stemmer.stem(lemma)
            processed_tokens.append(stem)
    
    # Збереження обробленого абзацу
    processed_paragraphs.append(" ".join(processed_tokens))

# Запис обробленого тексту у файл з явним вказанням кодування UTF-8
with open("output1.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(processed_paragraphs))
