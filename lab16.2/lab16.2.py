import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import regexp_tokenize
import string

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Function for text processing
def process_text(text):
    # Tokenization
    words = word_tokenize(text)

    # Remove punctuation
    words = [word for word in words if word not in string.punctuation]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    return words

# Reading the input text
with open('input_text.txt', 'r') as file:
    text = file.read()

# Process the text
processed_words = process_text(text)

# Write the processed text to a new file
with open('processed_text.txt', 'w') as file:
    file.write(" ".join(processed_words))

print("Text processing is complete. Processed text is saved in 'processed_text.txt'.")

