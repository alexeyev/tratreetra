""" Self-explanatory """
from enum import Enum


class UPOS(str, Enum):
    """ A list of all part-of-speech tags (UPOS) """
    ADJ = "ADJ"      # adjective
    ADP = "ADP"      # adposition
    ADV = "ADV"      # adverb
    AUX = "AUX"      # auxiliary
    CCONJ = "CCONJ"  # coordinating conjunction
    DET = "DET"      # determiner
    INTJ = "INTJ"    # interjection
    NOUN = "NOUN"    # noun
    NUM = "NUM"      # numeral
    PART = "PART"    # particle
    PRON = "PRON"    # pronoun
    PROPN = "PROPN"  # proper noun
    PUNCT = "PUNCT"  # punctuation
    SCONJ = "SCONJ"  # subordinating conjunction
    SYM = "SYM"      # symbol
    VERB = "VERB"    # verb
    X = "X"          # other
