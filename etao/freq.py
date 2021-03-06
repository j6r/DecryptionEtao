"""Letter frequencies by language"""

"""The following table is from https://en.wikipedia.org/wiki/Letter_frequency,
and is attributed to Robert Lewand's Cryptological Mathematics."""
ENGLISH_FREQ = {
    'e': 12.702,
    't': 9.056,
    'a': 8.167,
    'o': 7.507,
    'i': 6.966,
    'n': 6.749,
    's': 6.327,
    'h': 6.094,
    'r': 5.987,
    'd': 4.253,
    'l': 4.025,
    'c': 2.782,
    'u': 2.758,
    'm': 2.406,
    'w': 2.361,
    'f': 2.228,
    'g': 2.015,
    'y': 1.974,
    'p': 1.929,
    'b': 1.492,
    'v': 0.978,
    'k': 0.772,
    'j': 0.153,
    'x': 0.150,
    'q': 0.095,
    'z': 0.074
}

"""Taken from https://www.math.cornell.edu/~mec/2003-2004/
cryptography/subs/digraphs.html"""
ENGLISH_DIGRAMS = {
    'th': 1.52,
    'he': 1.28,
    'in': 0.94,
    'er': 0.94,
    'an': 0.82,
    're': 0.68,
    'nd': 0.63,
    'at': 0.59,
    'on': 0.57,
    'nt': 0.56,
    'ha': 0.56,
    'es': 0.56,
    'st': 0.55,
    'en': 0.55,
    'ed': 0.53,
    'to': 0.52,
    'it': 0.50,
    'ou': 0.50,
    'ea': 0.47,
    'hi': 0.46,
    'is': 0.46,
    'or': 0.43,
    'ti': 0.34,
    'as': 0.33,
    'te': 0.27,
    'et': 0.19,
    'ng': 0.18,
    'of': 0.16,
    'al': 0.09,
    'de': 0.09,
    'se': 0.08,
    'le': 0.08,
    'sa': 0.06,
    'si': 0.05,
    'ar': 0.04,
    've': 0.04,
    'ra': 0.04,
    'ld': 0.02,
    'ur': 0.02,
}
