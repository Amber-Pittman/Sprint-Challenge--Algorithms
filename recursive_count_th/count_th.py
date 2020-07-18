'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
start = 0
count = 0

def count_th(word):
    global count, start 
    # TBC
    if start + 2 > len(word):
        index_count = count
        count = 0 
        start = 0
        return index_count
    if word[start:start+2] == "th":
        count += 1
    start += 1
    return count_th(word)
