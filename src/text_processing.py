import nltk
import json
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from .config import SLANG_DICT_PATH

# Download required NLTK data quietly
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

# Initialize global tools
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Load slang dictionary
with open(SLANG_DICT_PATH, 'r') as f:
    slang_dict = json.load(f)

"""
Normalizes raw text into lemmatized vocabulary words.

Args:
    text (str): Cleaned text string.

Returns:
    list[str]: List of normalized vocabulary words.
"""
def normalize_text(words: list[str]) -> list[str]:

    # Replace slang
    normalized = [slang_dict.get(w, w) for w in words]

    # Remove stopwords and short tokens
    filtered = [w for w in normalized if w not in stop_words and len(w) > 2]

    # Lemmatize each word
    lemmatized = [lemmatizer.lemmatize(w) for w in filtered]

    return lemmatized