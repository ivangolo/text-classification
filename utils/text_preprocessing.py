"""
Utility function for text cleaning.
"""
import re
import string
import nltk
import emoji

def remove_tweet_user_mentions(text):
    """Remove twitter users from text."""
    return re.sub(r'@\S+', ' ', text, re.UNICODE)


def remove_tweet_hashtags(text):
    """Remove tweet hashtags."""
    return re.sub(r'#\S+', ' ', text, re.UNICODE)


def remove_links(text):
    """Remove links, urls from text."""
    return re.sub(r'(http|https)\S+', ' ', text, re.UNICODE)


def to_lower(text):
    """Convert text to lowercase."""
    return text.lower()


def remove_emojis(text):
    """Remove emojis (emoticons) from text."""
    return emoji.get_emoji_regexp().sub(' ', text)


def remove_punctuation(text):
    """Remove punctuation symbols."""
    punctuation_symbols = string.punctuation
    punctuation_symbols += '¿¡'
    text = text.replace('\u2026', ' ')  # triple dots
    text = text.replace('\u25ba', ' ')  # BLACK RIGHT-POINTING POINTER
    text = text.replace('\u201c', ' ')  # left double quote
    text = text.replace('\u201d', ' ')  # right double quote
    return text.translate(str.maketrans(' ', ' ', punctuation_symbols))


def remove_numbers(text):
    """Remove numeric characters."""
    return re.sub(r'\d+', ' ', text)


def remove_stopwords(text):
    """Remove stopwords from text"""
    stoplist = nltk.corpus.stopwords.words('spanish')
    stoplist.remove('no')
    stoplist.extend([
        'rt',
        'q',
        'd',
        'x'
    ])
    return ' '.join([w for w in text.split() if w not in stoplist])


def remove_extra_whites(text):
    """Remove white characters repetitions from text."""
    return ' '.join(text.split())


def remove_repeated_vowels(text):
    """Remove repeated vowels from each word."""
    return re.sub(r'([aeiou])\1+', r'\1', text, re.UNICODE)


def remove_repeated_consonants(text):
    """Remove repeated consonants from each word."""
    return re.sub(r'([bcdfghjkmnpqstvwxyz])\1+', r'\1', text, re.UNICODE)


def remove_repeated_consonants_spa(text):
    """
    In spanish there are words written with double l or double r.
    We give them a special treatment.
    """
    return re.sub(r'([lr])\1\1+', r'\1\1', text, re.UNICODE)


def remove_repeated_chars(text):
    text = remove_repeated_vowels(text)
    text = remove_repeated_consonants(text)
    return remove_repeated_consonants_spa(text)


def remove_laugh(text):
    """Remove laughing expressions such as ajaja... jajaj, etc."""
    return re.sub(r'\b(?:a*(?:ja)+j?|(?:l+o+)+l+)\b', ' ', text, re.UNICODE)


def normalize(text):
    text = remove_tweet_user_mentions(text)
    text = remove_tweet_hashtags(text)
    text = remove_links(text)
    text = to_lower(text)
    text = remove_punctuation(text)
    text = remove_stopwords(text)
    # text = remove_emojis(text)
    text = remove_numbers(text)
    text = remove_extra_whites(text)
    return text
