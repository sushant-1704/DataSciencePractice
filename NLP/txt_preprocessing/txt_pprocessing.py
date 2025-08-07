import re
import string
import emoji
import unicodedata
from bs4 import BeautifulSoup
import nltk
from spellchecker import SpellChecker  # NEW

# Download required NLTK resources (run once)
nltk.download('punkt')
nltk.download('punkt_tab')  # Fix for punkt_tab error
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize

# Initialize spell checker
spell = SpellChecker()

# Load data from file
with open('sample_nlp_texts.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Function: Clean HTML
def remove_html_tags(text):
    return BeautifulSoup(text, "html.parser").get_text()

# Function: Normalize unicode characters
def normalize_unicode(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

# Function: Remove URLs
def remove_urls(text):
    return re.sub(r'https?://\S+|www\.\S+', '', text)

# Function: Remove emojis
def remove_emojis(text):
    return emoji.replace_emoji(text, replace='')

# Function: Expand contractions
contractions = {
    "can't": "cannot", "won't": "will not", "n't": " not",
    "I'm": "I am", "I've": "I have", "we’re": "we are", "u": "you", "ur": "your",
    "dnt": "don't", "wht": "what", "gr8": "great", "IDK": "I don't know", "ppl": "people",
    "gonna": "going to", "gotta": "got to", "dunno": "do not know", "TY": "Thank you"
}

def expand_contractions(text):
    for key, value in contractions.items():
        text = re.sub(r'\b' + re.escape(key) + r'\b', value, text, flags=re.IGNORECASE)
    return text

# Function: Remove punctuation
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Function: Correct spelling
def correct_spelling(text):
    corrected_words = []
    for word in text.split():
        corrected_word = spell.correction(word)
        corrected_words.append(corrected_word)
    return ' '.join(corrected_words)

# Function: Tokenize
def tokenize_text(text):
    return word_tokenize(text)

# Function: Preprocess each line
def preprocess_text(text):
    print("Original:", text.strip())

    text = remove_html_tags(text)
    print("HTML removed:", text)

    text = normalize_unicode(text)
    print("Normalized:", text)

    text = remove_urls(text)
    print("URLs removed:", text)

    text = remove_emojis(text)
    print("Emojis removed:", text)

    text = expand_contractions(text)
    print("Contractions expanded:", text)

    text = text.lower()
    print("Lowercased:", text)

    text = remove_punctuation(text)
    print("Punctuation removed:", text)

    text = correct_spelling(text)
    print("Spelling corrected:", text)

    tokens = tokenize_text(text)
    print("Tokens:", tokens)

    print("===" * 20)
    return " ".join(tokens)

# Preprocess all lines
processed_lines = [preprocess_text(line) for line in lines]

# Save cleaned data
with open('cleaned_texts.txt', 'w', encoding='utf-8') as file:
    for line in processed_lines:
        file.write(line + "\n")