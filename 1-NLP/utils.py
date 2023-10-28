import re
from nltk.corpus import stopwords
from typing import List, Callable
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')

wn = WordNetLemmatizer()
sm = PorterStemmer()
# Handle Negation
en_stop_words = [w for w in stopwords.words(
    'english') if not re.search("not|n't", w)]


class Constant:
    """Holding Constant Values"""
    PAD_VAL = '[PAD]'
    OOV_VAL = '[OOV]'
    PAD_IDX = 0
    OOV_IDX = 1


def pipeline(x, *functions: Callable):
    """Calling Sequence of methods taking the input sequentially
    objective: a cleaner format of writing a hierarchical seq. of methods

        f5(f4(f3(f2(f1(x))))) --> pipeline(x, f1, f2, f3, f4, f5)
    Args:
        x (Any): any input

    Returns:
        Any: transformed output
    """
    ...
    return x


def to_lower(text: str) -> str:
    return ...


def tokenize_text(text: str) -> List[str]:
    return ...


def remove_stop_words(review_tokens: List[str]) -> List[str]:
    return ...


def stem(text_tokens: List[str]) -> List[str]:
    return ...


def preprocess_review(text: str) -> List[str]:
    """Apply Sequence of operations on the given text
        - clean_text: to lower & Lemmatize
        - remove_stop_words
        - tokenize: convert cleaned text --> list of tokens
    Args:
        text (str): user review in string format
    Returns:
        List[str]: user review cleaned and tokenized
    """
    return pipeline(text,
                    to_lower,
                    tokenize_text,
                    remove_stop_words,
                    stem)
