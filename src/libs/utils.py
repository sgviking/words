from collections import Counter
import re
import string


def count_words(text):
    '''
    Takes a string, counts the total number of words and the occurence
    of each word within the spring.  Ignores punctuation.

    Note: This will count numbers as a word.  For dealing with very large
    strings in a production environment this could be optimized by processing
    the strings in pieces.  Since this string comes from a POST request
    proxied in from NGINX this is limited by the size of allowed POST bodies.
    Currently this program can only handle ~12M of POST data before it runs out
    of memory on the production server (500M RAM).
    '''
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
