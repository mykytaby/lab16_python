import nltk
from nltk.corpus import stopwords
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt

# Ensure all necessary NLTK data is downloaded
try:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('gutenberg')
except Exception as e:
    print(f"Error downloading NLTK resources: {e}")
    exit(1)

# Load the text from Project Gutenberg
text = gutenberg.raw('austen-emma.txt')

# Function to count the total number of words in the text
def count_words(text):
    try:
        words = word_tokenize(text)
        return len(words)
    except LookupError:
        print("Please download the necessary NLTK resources.")
        exit(1)

# Function to find the 10 most frequent words and plot a bar chart
def most_used_words(text, title="10 Most Frequent Words in the Text"):
    words = word_tokenize(text)
    cnt = Counter(words)
    most_common = cnt.most_common(10)
    
    # Plot a bar chart
    x = [word[0] for word in most_common]  # Words
    y = [word[1] for word in most_common]  # Frequencies
    plt.bar(x, y, color='skyblue')
    plt.title(title)
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.show()

# Function to clean the text by removing stop words and punctuation
def clean_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    cleaned_words = [
        word.lower() for word in words if word.isalnum() and word.lower() not in stop_words
    ]
    return ' '.join(cleaned_words)

# Count the total number of words in the text
word_count = count_words(text)
print(f"Total word count: {word_count}")

# Plot a bar chart for the 10 most frequent words in the original text
print("Plotting most frequent words in the original text...")
most_used_words(text, "10 Most Frequent Words (Original Text)")

# Clean the text by removing punctuation and stop words
print("Cleaning text by removing punctuation and stop words...")
cleaned_text = clean_text(text)

# Plot a bar chart for the 10 most frequent words in the cleaned text
print("Plotting most frequent words after cleaning the text...")
most_used_words(cleaned_text, "10 Most Frequent Words (After Cleaning)")
