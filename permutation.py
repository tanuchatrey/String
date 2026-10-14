from typing import List

# Generate permutations using swapping
def recurPermute(index, s, res):
    if index == len(s):
        res.append(''.join(s))
        return

    for i in range(index, len(s)):
        s[index], s[i] = s[i], s[index]

        # fix current position and recurse
        recurPermute(index + 1, s, res)

        # backtrack
        s[index], s[i] = s[i], s[index]

def permutation(s):
    res = []

    s = list(s)

    recurPermute(0, s, res)

    # sort lexicographically
    res.sort()

    return res

if __name__ == '__main__':
    s = "AAB"

    res = permutation(s)

    for x in res: print(x, end=' ')
