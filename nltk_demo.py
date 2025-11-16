
import nltk


nltk.download('punkt')       
nltk.download('wordnet')     
nltk.download('omw-1.4')     

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer


text = "NLTK is a powerful library for natural language processing. It helps in tokenizing, stemming, and lemmatization."


print("\n--- Tokenization ---")
sentences = sent_tokenize(text)
words = word_tokenize(text)

print("Sentence Tokenization:", sentences)
print("Word Tokenization:", words)


print("\n--- Stemming ---")
ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in words]
print("Stemmed Words:", stemmed_words)


print("\n--- Lemmatization ---")
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print("Lemmatized Words:", lemmatized_words)
