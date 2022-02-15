def abbreviate(words):
    acronym = []
    words = words.replace('_', ' ')
    words = words.replace('-', ' ')
    words = words.split()
    for word in words:
        acronym.append(word[0])
    acronym = ''.join(acronym)
    return acronym.upper()
