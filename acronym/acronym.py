"""
Acronym
"""
def abbreviate(words):
    """
    Convert a phrase to its acronym.
    """
    acronym = []
    words = words.replace('_', ' ')
    words = words.replace('-', ' ')
    words = words.split()
    for word in words:
        acronym.append(word[0])
    acronym = ''.join(acronym)
    return acronym.upper()
