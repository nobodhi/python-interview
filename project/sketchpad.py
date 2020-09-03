import time
start = time.time()

def count_words(str):
    stop_chars = ',.'
    # strip out stop characters
    for char in stop_chars:
        if char in str:
            str = str.replace(char, '')
    # count each word into a dictionary
    counts = {}
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return [word for word in counts if counts[word] > 1]


start = time.time()
string = 'here is a word, and here is another word.'
print('count words', count_words(string))
print(round(time.time() - start, 2), "seconds elapsed")
