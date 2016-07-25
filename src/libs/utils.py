from collections import Counter
import re
import string


def count_words(text):
    # words = re.split(ur'\W+', text.lower())
    # words = filter(None, words)

    # regex from here: http://stackoverflow.com/a/12705513
    # match words, including words with apostrophes. Remove line endings
    words = re.split(ur"(\w[\w']*\w|\w)", text.lower().replace('\n', ' '))
    # Remove elements that are just spaces, strip punction according to locale
    words = [word.replace(' ', '').strip(string.punctuation) for word in words]
    words = filter(None, words)

    i = 0
    count = Counter()
    for word in words:
        count[word] += 1
        i += 1

    return {'count': i, 'words': count}
