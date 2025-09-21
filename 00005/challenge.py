"""
Question:

You are given a string formed by concatenating several words corresponding to the integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'. Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order. In the example above, this would be 357.

"""

from collections import Counter


def solution(s: str):
    count = Counter(s)
    out = {0: count['z'], 2: count['w'], 4: count['u'], 6: count['x'], 8: count['g']}

    # Deduce remaining
    out[1] = count['o'] - out[0] - out[2] - out[4]
    out[3] = count['h'] - out[8]
    out[5] = count['f'] - out[4]
    out[7] = count['s'] - out[6]
    out[9] = count['i'] - out[5] - out[6] - out[8]

    # Build output
    result = int(''.join(str(i) * out[i] for i in range(10)))
    return result


print(solution('niesevehrtfeev'))
