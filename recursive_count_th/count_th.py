'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    # base case
    if "th" not in word:
        # return zero instances
        return 0
    # if the first two letters in the string are "th"
    if "th" in word[0:2]:
        # count them and recursively call the function iterating the index by 1,
        # and adding 1 as a count
        return count_th(word[1:]) + 1
    # else:
    else:
        # recursively call the function, iterate to the next pair in the list,
        # and check again for "th"
        return count_th(word[1:])
