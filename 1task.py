import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt

# Завантаження тексту з файлу
with open('austen-sense.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Токенізація тексту
words = word_tokenize(text)

# Виведення кількості слів до видалення стоп-слів та пунктуації
print("Кількість слів у тексті (до видалення стоп-слів та пунктуації):", len(words))

# Видалення пунктуації та стоп-слів
stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

# Визначення кількості слів
word_count = len(filtered_words)
print("Кількість слів у тексті (після видалення стоп-слів та пунктуації):", word_count)

# Знаходження 10 найбільш вживаних слів
word_freq = Counter(filtered_words)
top_words = word_freq.most_common(10)
print("10 найбільш вживаних слів у тексті (після видалення стоп-слів та пунктуації):", top_words)

# Побудова стовпчастої діаграми
words, frequencies = zip(*top_words)
plt.figure(figsize=(10, 6))
plt.bar(words, frequencies, color='skyblue')
plt.title('10 найбільш вживаних слів у тексті')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
