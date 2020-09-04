import time
start = time.time()

def count_words(str):
    '''count any words that occur more than once. we can use a counting dictionary or a set approach.'''
    stop_chars = ',.'
    # strip out stop characters
    for char in stop_chars:
        if char in str:
            str = str.replace(char, '')
    # set approach
    unique = set()
    repeated = set()
    words = str.split()
    for word in words:
        if word in unique:
            if word not in repeated:
                repeated.add(word)
        else:
            unique.add(word)
    return repeated


start = time.time()
string = 'here is a word, and here is another word.'
print('count words', count_words(string))
print(round(time.time() - start, 2), "seconds elapsed")
