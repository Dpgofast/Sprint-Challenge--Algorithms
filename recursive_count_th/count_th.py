'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur
within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) < 2:
        return 0  # cant have a 2 letter word if the word is a single letter..

    # Check pairs of letters for matching pattern
    elif (word[0:2] == 'th'):
        # declaring the pattern lowercase for case sensitivity
        return count_th(word[1:]) + 1
    else:
        return count_th(word[1:])
